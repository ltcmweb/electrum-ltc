# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mwebd_pb2 as mwebd__pb2


class RpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Status = channel.unary_unary(
                '/Rpc/Status',
                request_serializer=mwebd__pb2.StatusRequest.SerializeToString,
                response_deserializer=mwebd__pb2.StatusResponse.FromString,
                )
        self.Utxos = channel.unary_stream(
                '/Rpc/Utxos',
                request_serializer=mwebd__pb2.UtxosRequest.SerializeToString,
                response_deserializer=mwebd__pb2.Utxo.FromString,
                )
        self.Addresses = channel.unary_unary(
                '/Rpc/Addresses',
                request_serializer=mwebd__pb2.AddressRequest.SerializeToString,
                response_deserializer=mwebd__pb2.AddressResponse.FromString,
                )
        self.LedgerKeys = channel.unary_unary(
                '/Rpc/LedgerKeys',
                request_serializer=mwebd__pb2.LedgerKeysRequest.SerializeToString,
                response_deserializer=mwebd__pb2.LedgerKeysResponse.FromString,
                )
        self.Spent = channel.unary_unary(
                '/Rpc/Spent',
                request_serializer=mwebd__pb2.SpentRequest.SerializeToString,
                response_deserializer=mwebd__pb2.SpentResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/Rpc/Create',
                request_serializer=mwebd__pb2.CreateRequest.SerializeToString,
                response_deserializer=mwebd__pb2.CreateResponse.FromString,
                )
        self.LedgerExchange = channel.unary_unary(
                '/Rpc/LedgerExchange',
                request_serializer=mwebd__pb2.LedgerApdu.SerializeToString,
                response_deserializer=mwebd__pb2.LedgerApdu.FromString,
                )
        self.Broadcast = channel.unary_unary(
                '/Rpc/Broadcast',
                request_serializer=mwebd__pb2.BroadcastRequest.SerializeToString,
                response_deserializer=mwebd__pb2.BroadcastResponse.FromString,
                )


class RpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Status(self, request, context):
        """Get the sync status of the daemon. The block headers are
        synced first, followed by a subset of MWEB headers, and
        finally the MWEB utxo set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Utxos(self, request, context):
        """Get a continuous stream of unspent MWEB outputs (utxos)
        for an account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Addresses(self, request, context):
        """Get a batch of MWEB addresses for an account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LedgerKeys(self, request, context):
        """Get the scan secret and spend pubkey from a Ledger
        for a given HD path.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Spent(self, request, context):
        """Check whether MWEB outputs are in the unspent set or not.
        This is used to determine when outputs have been spent by
        either this or another wallet using the same seed, and to
        determine when MWEB transactions have confirmed by checking
        the output IDs of the MWEB inputs and outputs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create the MWEB portion of a transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LedgerExchange(self, request, context):
        """Process APDUs from the Ledger.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Broadcast(self, request, context):
        """Broadcast a transaction to the network. This is provided as
        existing broadcast services may not support MWEB transactions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=mwebd__pb2.StatusRequest.FromString,
                    response_serializer=mwebd__pb2.StatusResponse.SerializeToString,
            ),
            'Utxos': grpc.unary_stream_rpc_method_handler(
                    servicer.Utxos,
                    request_deserializer=mwebd__pb2.UtxosRequest.FromString,
                    response_serializer=mwebd__pb2.Utxo.SerializeToString,
            ),
            'Addresses': grpc.unary_unary_rpc_method_handler(
                    servicer.Addresses,
                    request_deserializer=mwebd__pb2.AddressRequest.FromString,
                    response_serializer=mwebd__pb2.AddressResponse.SerializeToString,
            ),
            'LedgerKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.LedgerKeys,
                    request_deserializer=mwebd__pb2.LedgerKeysRequest.FromString,
                    response_serializer=mwebd__pb2.LedgerKeysResponse.SerializeToString,
            ),
            'Spent': grpc.unary_unary_rpc_method_handler(
                    servicer.Spent,
                    request_deserializer=mwebd__pb2.SpentRequest.FromString,
                    response_serializer=mwebd__pb2.SpentResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=mwebd__pb2.CreateRequest.FromString,
                    response_serializer=mwebd__pb2.CreateResponse.SerializeToString,
            ),
            'LedgerExchange': grpc.unary_unary_rpc_method_handler(
                    servicer.LedgerExchange,
                    request_deserializer=mwebd__pb2.LedgerApdu.FromString,
                    response_serializer=mwebd__pb2.LedgerApdu.SerializeToString,
            ),
            'Broadcast': grpc.unary_unary_rpc_method_handler(
                    servicer.Broadcast,
                    request_deserializer=mwebd__pb2.BroadcastRequest.FromString,
                    response_serializer=mwebd__pb2.BroadcastResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Rpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Rpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Status',
            mwebd__pb2.StatusRequest.SerializeToString,
            mwebd__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Utxos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Rpc/Utxos',
            mwebd__pb2.UtxosRequest.SerializeToString,
            mwebd__pb2.Utxo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Addresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Addresses',
            mwebd__pb2.AddressRequest.SerializeToString,
            mwebd__pb2.AddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LedgerKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/LedgerKeys',
            mwebd__pb2.LedgerKeysRequest.SerializeToString,
            mwebd__pb2.LedgerKeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Spent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Spent',
            mwebd__pb2.SpentRequest.SerializeToString,
            mwebd__pb2.SpentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Create',
            mwebd__pb2.CreateRequest.SerializeToString,
            mwebd__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LedgerExchange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/LedgerExchange',
            mwebd__pb2.LedgerApdu.SerializeToString,
            mwebd__pb2.LedgerApdu.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Broadcast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Broadcast',
            mwebd__pb2.BroadcastRequest.SerializeToString,
            mwebd__pb2.BroadcastResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
