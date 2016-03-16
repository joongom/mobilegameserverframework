# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_packet_play.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import msg_error_pb2
import msg_struct_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_packet_play.proto',
  package='msg',
  serialized_pb=_b('\n\x15msg_packet_play.proto\x12\x03msg\x1a\x0fmsg_error.proto\x1a\x10msg_struct.proto\"7\n\x0e\x65nter_town_req\x12\x12\n\nauth_token\x18\x01 \x02(\t\x12\x11\n\tchar_name\x18\x02 \x02(\t\"Q\n\x0e\x65nter_town_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12\x1e\n\x08init_pos\x18\x02 \x02(\x0b\x32\x0c.msg.vector3')
  ,
  dependencies=[msg_error_pb2.DESCRIPTOR,msg_struct_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENTER_TOWN_REQ = _descriptor.Descriptor(
  name='enter_town_req',
  full_name='msg.enter_town_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.enter_town_req.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_name', full_name='msg.enter_town_req.char_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=120,
)


_ENTER_TOWN_ACK = _descriptor.Descriptor(
  name='enter_town_ack',
  full_name='msg.enter_town_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.enter_town_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_pos', full_name='msg.enter_town_ack.init_pos', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=203,
)

_ENTER_TOWN_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_ENTER_TOWN_ACK.fields_by_name['init_pos'].message_type = msg_struct_pb2._VECTOR3
DESCRIPTOR.message_types_by_name['enter_town_req'] = _ENTER_TOWN_REQ
DESCRIPTOR.message_types_by_name['enter_town_ack'] = _ENTER_TOWN_ACK

enter_town_req = _reflection.GeneratedProtocolMessageType('enter_town_req', (_message.Message,), dict(
  DESCRIPTOR = _ENTER_TOWN_REQ,
  __module__ = 'msg_packet_play_pb2'
  # @@protoc_insertion_point(class_scope:msg.enter_town_req)
  ))
_sym_db.RegisterMessage(enter_town_req)

enter_town_ack = _reflection.GeneratedProtocolMessageType('enter_town_ack', (_message.Message,), dict(
  DESCRIPTOR = _ENTER_TOWN_ACK,
  __module__ = 'msg_packet_play_pb2'
  # @@protoc_insertion_point(class_scope:msg.enter_town_ack)
  ))
_sym_db.RegisterMessage(enter_town_ack)


# @@protoc_insertion_point(module_scope)
