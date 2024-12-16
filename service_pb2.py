# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\tmyservice\"M\n\x13RegisterRoomRequest\x12\x13\n\x0broom_number\x18\x01 \x01(\x05\x12\x11\n\troom_type\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"8\n\x14RegisterRoomResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07room_id\x18\x02 \x01(\x05\":\n\x17UpdateRoomStatusRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"+\n\x18UpdateRoomStatusResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\x12GetRoomByIdRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\"^\n\x13GetRoomByIdResponse\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\x12\x13\n\x0broom_number\x18\x02 \x01(\x05\x12\x11\n\troom_type\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"*\n\x13GetRoomByNumRequest\x12\x13\n\x0broom_number\x18\x01 \x01(\x05\"_\n\x14GetRoomByNumResponse\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\x12\x13\n\x0broom_number\x18\x02 \x01(\x05\x12\x11\n\troom_type\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t2\xd8\x02\n\tMyService\x12O\n\x0cRegisterRoom\x12\x1e.myservice.RegisterRoomRequest\x1a\x1f.myservice.RegisterRoomResponse\x12[\n\x10UpdateRoomStatus\x12\".myservice.UpdateRoomStatusRequest\x1a#.myservice.UpdateRoomStatusResponse\x12L\n\x0bGetRoomById\x12\x1d.myservice.GetRoomByIdRequest\x1a\x1e.myservice.GetRoomByIdResponse\x12O\n\x0cGetRoomByNum\x12\x1e.myservice.GetRoomByNumRequest\x1a\x1f.myservice.GetRoomByNumResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERROOMREQUEST']._serialized_start=28
  _globals['_REGISTERROOMREQUEST']._serialized_end=105
  _globals['_REGISTERROOMRESPONSE']._serialized_start=107
  _globals['_REGISTERROOMRESPONSE']._serialized_end=163
  _globals['_UPDATEROOMSTATUSREQUEST']._serialized_start=165
  _globals['_UPDATEROOMSTATUSREQUEST']._serialized_end=223
  _globals['_UPDATEROOMSTATUSRESPONSE']._serialized_start=225
  _globals['_UPDATEROOMSTATUSRESPONSE']._serialized_end=268
  _globals['_GETROOMBYIDREQUEST']._serialized_start=270
  _globals['_GETROOMBYIDREQUEST']._serialized_end=307
  _globals['_GETROOMBYIDRESPONSE']._serialized_start=309
  _globals['_GETROOMBYIDRESPONSE']._serialized_end=403
  _globals['_GETROOMBYNUMREQUEST']._serialized_start=405
  _globals['_GETROOMBYNUMREQUEST']._serialized_end=447
  _globals['_GETROOMBYNUMRESPONSE']._serialized_start=449
  _globals['_GETROOMBYNUMRESPONSE']._serialized_end=544
  _globals['_MYSERVICE']._serialized_start=547
  _globals['_MYSERVICE']._serialized_end=891
# @@protoc_insertion_point(module_scope)