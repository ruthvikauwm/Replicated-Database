# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import raft_pb2 as raft__pb2


class RaftStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VoteRequest = channel.unary_unary(
                '/Raft/VoteRequest',
                request_serializer=raft__pb2.vote_4_me.SerializeToString,
                response_deserializer=raft__pb2.voted_4_u.FromString,
                )
        self.AppendEntryRequest = channel.unary_unary(
                '/Raft/AppendEntryRequest',
                request_serializer=raft__pb2.appendEntry.SerializeToString,
                response_deserializer=raft__pb2.appendEntry_pending.FromString,
                )
        self.heartbeatUpdate = channel.unary_unary(
                '/Raft/heartbeatUpdate',
                request_serializer=raft__pb2.heartbeat.SerializeToString,
                response_deserializer=raft__pb2.heartbeat_response.FromString,
                )
        self.getVal = channel.unary_unary(
                '/Raft/getVal',
                request_serializer=raft__pb2.getVal_request.SerializeToString,
                response_deserializer=raft__pb2.getVal_response.FromString,
                )
        self.setVal = channel.unary_unary(
                '/Raft/setVal',
                request_serializer=raft__pb2.setVal_request.SerializeToString,
                response_deserializer=raft__pb2.setVal_response.FromString,
                )
        self.suspend = channel.unary_unary(
                '/Raft/suspend',
                request_serializer=raft__pb2.suspend_request.SerializeToString,
                response_deserializer=raft__pb2.suspend_response.FromString,
                )
        self.commitVal = channel.unary_unary(
                '/Raft/commitVal',
                request_serializer=raft__pb2.commitVal_request.SerializeToString,
                response_deserializer=raft__pb2.commitVal_response.FromString,
                )


class RaftServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VoteRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppendEntryRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def heartbeatUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getVal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setVal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def suspend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def commitVal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RaftServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VoteRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteRequest,
                    request_deserializer=raft__pb2.vote_4_me.FromString,
                    response_serializer=raft__pb2.voted_4_u.SerializeToString,
            ),
            'AppendEntryRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendEntryRequest,
                    request_deserializer=raft__pb2.appendEntry.FromString,
                    response_serializer=raft__pb2.appendEntry_pending.SerializeToString,
            ),
            'heartbeatUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.heartbeatUpdate,
                    request_deserializer=raft__pb2.heartbeat.FromString,
                    response_serializer=raft__pb2.heartbeat_response.SerializeToString,
            ),
            'getVal': grpc.unary_unary_rpc_method_handler(
                    servicer.getVal,
                    request_deserializer=raft__pb2.getVal_request.FromString,
                    response_serializer=raft__pb2.getVal_response.SerializeToString,
            ),
            'setVal': grpc.unary_unary_rpc_method_handler(
                    servicer.setVal,
                    request_deserializer=raft__pb2.setVal_request.FromString,
                    response_serializer=raft__pb2.setVal_response.SerializeToString,
            ),
            'suspend': grpc.unary_unary_rpc_method_handler(
                    servicer.suspend,
                    request_deserializer=raft__pb2.suspend_request.FromString,
                    response_serializer=raft__pb2.suspend_response.SerializeToString,
            ),
            'commitVal': grpc.unary_unary_rpc_method_handler(
                    servicer.commitVal,
                    request_deserializer=raft__pb2.commitVal_request.FromString,
                    response_serializer=raft__pb2.commitVal_response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Raft', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Raft(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VoteRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/VoteRequest',
            raft__pb2.vote_4_me.SerializeToString,
            raft__pb2.voted_4_u.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppendEntryRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/AppendEntryRequest',
            raft__pb2.appendEntry.SerializeToString,
            raft__pb2.appendEntry_pending.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def heartbeatUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/heartbeatUpdate',
            raft__pb2.heartbeat.SerializeToString,
            raft__pb2.heartbeat_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getVal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/getVal',
            raft__pb2.getVal_request.SerializeToString,
            raft__pb2.getVal_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setVal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/setVal',
            raft__pb2.setVal_request.SerializeToString,
            raft__pb2.setVal_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def suspend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/suspend',
            raft__pb2.suspend_request.SerializeToString,
            raft__pb2.suspend_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def commitVal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Raft/commitVal',
            raft__pb2.commitVal_request.SerializeToString,
            raft__pb2.commitVal_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
