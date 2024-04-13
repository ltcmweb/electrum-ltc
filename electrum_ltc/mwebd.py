from contextlib import closing
import grpc
import os
from pathlib import Path
import socket
import subprocess
import threading

from .bitcoin import is_mweb_address
from . import constants
from .transaction import PartialTransaction, Transaction
from .mwebd_pb2 import CreateRequest, StatusRequest
from .mwebd_pb2_grpc import RpcStub
from .util import user_dir

lock = threading.Lock()
port = None
process = None

def find_free_port():
    global port
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('127.0.0.1', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        port = s.getsockname()[1]

def start_if_needed():
    with lock: _start_if_needed()

def _start_if_needed():
    global process
    if process is None:
        find_free_port()
        data_dir = user_dir()
        network = constants.net.NET_NAME
        if network != 'mainnet':
            data_dir = os.path.join(data_dir, network)
        data_dir = os.path.join(data_dir, 'mweb')
        Path(data_dir).mkdir(parents=True, exist_ok=True)
        args = ['mwebd', '-c', network, '-d', data_dir,
                '-l', str(port), '-ppid', str(os.getpid())]
        process = subprocess.Popen(args, stdout=subprocess.DEVNULL)

        while True:
            try:
                RpcStub(grpc.insecure_channel(f'127.0.0.1:{port}')).Status(StatusRequest())
                break
            except: ()

def stub():
    start_if_needed()
    return RpcStub(grpc.insecure_channel(f'127.0.0.1:{port}'))

def stub_async():
    start_if_needed()
    return RpcStub(grpc.aio.insecure_channel(f'127.0.0.1:{port}'))

def create(tx, scan_secret, spend_secret, fee_estimator, *, dry_run = False):
    raw_tx = bytes.fromhex(tx.serialize_to_network(include_sigs=False))
    resp = stub().Create(CreateRequest(raw_tx=raw_tx,
        scan_secret=scan_secret, spend_secret=spend_secret,
        fee_rate_per_kb=fee_estimator(1000), dry_run=dry_run))
    if resp.raw_tx == raw_tx: return tx, 0
    tx2 = PartialTransaction.from_tx(Transaction(resp.raw_tx))
    for i, txin in enumerate(tx2.inputs()):
        tx2.inputs()[i] = next(x for x in tx.inputs() if str(x.prevout) == str(txin.prevout))
    mweb_input = tx.input_value() - tx2.input_value()
    expected_pegin = max(0, tx.output_value() - mweb_input)
    fee_increase = tx2.output_value() - expected_pegin
    if expected_pegin: fee_increase += fee_estimator(41)
    for txout in tx.outputs():
        if is_mweb_address(txout.address) and not dry_run:
            txout.mweb_output_id = resp.output_id.pop(0)
    tx2._original_tx = tx
    return tx2, fee_increase
