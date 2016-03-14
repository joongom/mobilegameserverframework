# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_error.proto',
  package='msg',
  serialized_pb=_b('\n\x0fmsg_error.proto\x12\x03msg*\xa2\x02\n\x08\x65rr_type\x12\x0c\n\x08\x65rr_none\x10\x00\x12\x17\n\x12\x65rr_server_unknown\x10\x90N\x12\x1c\n\x17\x65rr_server_unauthorized\x10\x91N\x12$\n\x1f\x65rr_server_user_userid_required\x10\xddV\x12$\n\x1f\x65rr_server_user_passwd_required\x10\xdeV\x12\x18\n\x12\x65rr_client_unknown\x10\xa0\x9c\x01\x12\x1d\n\x17\x65rr_client_unauthorized\x10\xa1\x9c\x01\x12%\n\x1f\x65rr_client_user_userid_required\x10\xed\xa4\x01\x12%\n\x1f\x65rr_client_user_passwd_required\x10\xee\xa4\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ERR_TYPE = _descriptor.EnumDescriptor(
  name='err_type',
  full_name='msg.err_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='err_none', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_server_unknown', index=1, number=10000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_server_unauthorized', index=2, number=10001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_server_user_userid_required', index=3, number=11101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_server_user_passwd_required', index=4, number=11102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_client_unknown', index=5, number=20000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_client_unauthorized', index=6, number=20001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_client_user_userid_required', index=7, number=21101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='err_client_user_passwd_required', index=8, number=21102,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=25,
  serialized_end=315,
)
_sym_db.RegisterEnumDescriptor(_ERR_TYPE)

err_type = enum_type_wrapper.EnumTypeWrapper(_ERR_TYPE)
err_none = 0
err_server_unknown = 10000
err_server_unauthorized = 10001
err_server_user_userid_required = 11101
err_server_user_passwd_required = 11102
err_client_unknown = 20000
err_client_unauthorized = 20001
err_client_user_userid_required = 21101
err_client_user_passwd_required = 21102


DESCRIPTOR.enum_types_by_name['err_type'] = _ERR_TYPE


# @@protoc_insertion_point(module_scope)
