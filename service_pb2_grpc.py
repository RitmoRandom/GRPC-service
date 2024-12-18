# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import service_pb2 as service__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterRoom = channel.unary_unary(
                '/myservice.MyService/RegisterRoom',
                request_serializer=service__pb2.RegisterRoomRequest.SerializeToString,
                response_deserializer=service__pb2.RegisterRoomResponse.FromString,
                _registered_method=True)
        self.UpdateRoomStatus = channel.unary_unary(
                '/myservice.MyService/UpdateRoomStatus',
                request_serializer=service__pb2.UpdateRoomStatusRequest.SerializeToString,
                response_deserializer=service__pb2.UpdateRoomStatusResponse.FromString,
                _registered_method=True)
        self.GetRoomById = channel.unary_unary(
                '/myservice.MyService/GetRoomById',
                request_serializer=service__pb2.GetRoomByIdRequest.SerializeToString,
                response_deserializer=service__pb2.GetRoomByIdResponse.FromString,
                _registered_method=True)
        self.GetRoomByNum = channel.unary_unary(
                '/myservice.MyService/GetRoomByNum',
                request_serializer=service__pb2.GetRoomByNumRequest.SerializeToString,
                response_deserializer=service__pb2.GetRoomByNumResponse.FromString,
                _registered_method=True)


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRoomStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoomById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoomByNum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterRoom,
                    request_deserializer=service__pb2.RegisterRoomRequest.FromString,
                    response_serializer=service__pb2.RegisterRoomResponse.SerializeToString,
            ),
            'UpdateRoomStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRoomStatus,
                    request_deserializer=service__pb2.UpdateRoomStatusRequest.FromString,
                    response_serializer=service__pb2.UpdateRoomStatusResponse.SerializeToString,
            ),
            'GetRoomById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoomById,
                    request_deserializer=service__pb2.GetRoomByIdRequest.FromString,
                    response_serializer=service__pb2.GetRoomByIdResponse.SerializeToString,
            ),
            'GetRoomByNum': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoomByNum,
                    request_deserializer=service__pb2.GetRoomByNumRequest.FromString,
                    response_serializer=service__pb2.GetRoomByNumResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'myservice.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('myservice.MyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/myservice.MyService/RegisterRoom',
            service__pb2.RegisterRoomRequest.SerializeToString,
            service__pb2.RegisterRoomResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRoomStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/myservice.MyService/UpdateRoomStatus',
            service__pb2.UpdateRoomStatusRequest.SerializeToString,
            service__pb2.UpdateRoomStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRoomById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/myservice.MyService/GetRoomById',
            service__pb2.GetRoomByIdRequest.SerializeToString,
            service__pb2.GetRoomByIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRoomByNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/myservice.MyService/GetRoomByNum',
            service__pb2.GetRoomByNumRequest.SerializeToString,
            service__pb2.GetRoomByNumResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
