# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_struct.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import msg_enum_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_struct.proto',
  package='msg',
  serialized_pb=_b('\n\x10msg_struct.proto\x12\x03msg\x1a\x0emsg_enum.proto\"*\n\x07vector3\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"\x1b\n\tchar_info\x12\x0e\n\x06\x63harid\x18\x01 \x02(\x04\"<\n\nequip_item\x12\x0e\n\x06itemid\x18\x01 \x02(\x04\x12\x1e\n\x06p_type\x18\x02 \x02(\x0e\x32\x0e.msg.part_type')
  ,
  dependencies=[msg_enum_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VECTOR3 = _descriptor.Descriptor(
  name='vector3',
  full_name='msg.vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='msg.vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='msg.vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='msg.vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=41,
  serialized_end=83,
)


_CHAR_INFO = _descriptor.Descriptor(
  name='char_info',
  full_name='msg.char_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='charid', full_name='msg.char_info.charid', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=85,
  serialized_end=112,
)


_EQUIP_ITEM = _descriptor.Descriptor(
  name='equip_item',
  full_name='msg.equip_item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemid', full_name='msg.equip_item.itemid', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p_type', full_name='msg.equip_item.p_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=114,
  serialized_end=174,
)

_EQUIP_ITEM.fields_by_name['p_type'].enum_type = msg_enum_pb2._PART_TYPE
DESCRIPTOR.message_types_by_name['vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['char_info'] = _CHAR_INFO
DESCRIPTOR.message_types_by_name['equip_item'] = _EQUIP_ITEM

vector3 = _reflection.GeneratedProtocolMessageType('vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.vector3)
  ))
_sym_db.RegisterMessage(vector3)

char_info = _reflection.GeneratedProtocolMessageType('char_info', (_message.Message,), dict(
  DESCRIPTOR = _CHAR_INFO,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.char_info)
  ))
_sym_db.RegisterMessage(char_info)

equip_item = _reflection.GeneratedProtocolMessageType('equip_item', (_message.Message,), dict(
  DESCRIPTOR = _EQUIP_ITEM,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.equip_item)
  ))
_sym_db.RegisterMessage(equip_item)


# @@protoc_insertion_point(module_scope)