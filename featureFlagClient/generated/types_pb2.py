# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='types.proto',
  package='featureflag.services.types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0btypes.proto\x12\x1a\x66\x65\x61tureflag.services.types\x1a google/protobuf/descriptor.proto:/\n\x07version\x12\x1c.google.protobuf.FileOptions\x18\xd0\x86\x03 \x01(\tb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


VERSION_FIELD_NUMBER = 50000
version = _descriptor.FieldDescriptor(
  name='version', full_name='featureflag.services.types.version', index=0,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['version'] = version
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(version)

# @@protoc_insertion_point(module_scope)
