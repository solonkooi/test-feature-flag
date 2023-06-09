# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FeatureFlagService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='FeatureFlagService.proto',
  package='featureflag.services.types',
  syntax='proto3',
  serialized_options=b'\252\002\032FeatureFlag.Services.Types\202\265\030\0051.4.0',
  serialized_pb=b'\n\x18\x46\x65\x61tureFlagService.proto\x12\x1a\x66\x65\x61tureflag.services.types\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0btypes.proto\"}\n\x15SetFeatureFlagRequest\x12\x1b\n\x13station_external_id\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x04 \x01(\x08\"\x18\n\x16SetFeatureFlagResponse\"d\n\x15GetFeatureFlagRequest\x12\x1b\n\x13station_external_id\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\"S\n\x16GetFeatureFlagResponse\x12 \n\x18\x66\x65\x61ture_flag_external_id\x18\x01 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x02 \x01(\x08\"\x85\x01\n\x18\x44\x65leteFeatureFlagRequest\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x39\n\x13station_external_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x1b\n\x19\x44\x65leteFeatureFlagResponse\"\x89\x01\n SetFeatureFlagForStationsRequest\x12\x1c\n\x14station_external_ids\x18\x01 \x03(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x04 \x01(\x08\"#\n!SetFeatureFlagForStationsResponse\"v\n&IsFeatureFlagEnabledForStationsRequest\x12\x1c\n\x14station_external_ids\x18\x01 \x03(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\"G\n\'IsFeatureFlagEnabledForStationsResponse\x12\x1c\n\x14station_external_ids\x18\x01 \x03(\t2\xd1\x05\n\x12\x46\x65\x61tureFlagService\x12w\n\x0eGetFeatureFlag\x12\x31.featureflag.services.types.GetFeatureFlagRequest\x1a\x32.featureflag.services.types.GetFeatureFlagResponse\x12w\n\x0eSetFeatureFlag\x12\x31.featureflag.services.types.SetFeatureFlagRequest\x1a\x32.featureflag.services.types.SetFeatureFlagResponse\x12\x80\x01\n\x11\x44\x65leteFeatureFlag\x12\x34.featureflag.services.types.DeleteFeatureFlagRequest\x1a\x35.featureflag.services.types.DeleteFeatureFlagResponse\x12\x98\x01\n\x19SetFeatureFlagForStations\x12<.featureflag.services.types.SetFeatureFlagForStationsRequest\x1a=.featureflag.services.types.SetFeatureFlagForStationsResponse\x12\xaa\x01\n\x1fIsFeatureFlagEnabledForStations\x12\x42.featureflag.services.types.IsFeatureFlagEnabledForStationsRequest\x1a\x43.featureflag.services.types.IsFeatureFlagEnabledForStationsResponseB&\xaa\x02\x1a\x46\x65\x61tureFlag.Services.Types\x82\xb5\x18\x05\x31.4.0b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,types__pb2.DESCRIPTOR,])




_SETFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='SetFeatureFlagRequest',
  full_name='featureflag.services.types.SetFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_external_id', full_name='featureflag.services.types.SetFeatureFlagRequest.station_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='featureflag.services.types.SetFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='featureflag.services.types.SetFeatureFlagRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='featureflag.services.types.SetFeatureFlagRequest.feature_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=226,
)


_SETFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='SetFeatureFlagResponse',
  full_name='featureflag.services.types.SetFeatureFlagResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=252,
)


_GETFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='GetFeatureFlagRequest',
  full_name='featureflag.services.types.GetFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_external_id', full_name='featureflag.services.types.GetFeatureFlagRequest.station_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='featureflag.services.types.GetFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='featureflag.services.types.GetFeatureFlagRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=354,
)


_GETFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='GetFeatureFlagResponse',
  full_name='featureflag.services.types.GetFeatureFlagResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_flag_external_id', full_name='featureflag.services.types.GetFeatureFlagResponse.feature_flag_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='featureflag.services.types.GetFeatureFlagResponse.feature_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=439,
)


_DELETEFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='DeleteFeatureFlagRequest',
  full_name='featureflag.services.types.DeleteFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='featureflag.services.types.DeleteFeatureFlagRequest.feature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='featureflag.services.types.DeleteFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='station_external_id', full_name='featureflag.services.types.DeleteFeatureFlagRequest.station_external_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=575,
)


_DELETEFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='DeleteFeatureFlagResponse',
  full_name='featureflag.services.types.DeleteFeatureFlagResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=604,
)


_SETFEATUREFLAGFORSTATIONSREQUEST = _descriptor.Descriptor(
  name='SetFeatureFlagForStationsRequest',
  full_name='featureflag.services.types.SetFeatureFlagForStationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_external_ids', full_name='featureflag.services.types.SetFeatureFlagForStationsRequest.station_external_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='featureflag.services.types.SetFeatureFlagForStationsRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='featureflag.services.types.SetFeatureFlagForStationsRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='featureflag.services.types.SetFeatureFlagForStationsRequest.feature_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=744,
)


_SETFEATUREFLAGFORSTATIONSRESPONSE = _descriptor.Descriptor(
  name='SetFeatureFlagForStationsResponse',
  full_name='featureflag.services.types.SetFeatureFlagForStationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=746,
  serialized_end=781,
)


_ISFEATUREFLAGENABLEDFORSTATIONSREQUEST = _descriptor.Descriptor(
  name='IsFeatureFlagEnabledForStationsRequest',
  full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_external_ids', full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsRequest.station_external_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=783,
  serialized_end=901,
)


_ISFEATUREFLAGENABLEDFORSTATIONSRESPONSE = _descriptor.Descriptor(
  name='IsFeatureFlagEnabledForStationsResponse',
  full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_external_ids', full_name='featureflag.services.types.IsFeatureFlagEnabledForStationsResponse.station_external_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=903,
  serialized_end=974,
)

_DELETEFEATUREFLAGREQUEST.fields_by_name['station_external_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['SetFeatureFlagRequest'] = _SETFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['SetFeatureFlagResponse'] = _SETFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureFlagRequest'] = _GETFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['GetFeatureFlagResponse'] = _GETFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['DeleteFeatureFlagRequest'] = _DELETEFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['DeleteFeatureFlagResponse'] = _DELETEFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['SetFeatureFlagForStationsRequest'] = _SETFEATUREFLAGFORSTATIONSREQUEST
DESCRIPTOR.message_types_by_name['SetFeatureFlagForStationsResponse'] = _SETFEATUREFLAGFORSTATIONSRESPONSE
DESCRIPTOR.message_types_by_name['IsFeatureFlagEnabledForStationsRequest'] = _ISFEATUREFLAGENABLEDFORSTATIONSREQUEST
DESCRIPTOR.message_types_by_name['IsFeatureFlagEnabledForStationsResponse'] = _ISFEATUREFLAGENABLEDFORSTATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('SetFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGREQUEST,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.SetFeatureFlagRequest)
  })
_sym_db.RegisterMessage(SetFeatureFlagRequest)

SetFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('SetFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGRESPONSE,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.SetFeatureFlagResponse)
  })
_sym_db.RegisterMessage(SetFeatureFlagResponse)

GetFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('GetFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATUREFLAGREQUEST,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.GetFeatureFlagRequest)
  })
_sym_db.RegisterMessage(GetFeatureFlagRequest)

GetFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('GetFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATUREFLAGRESPONSE,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.GetFeatureFlagResponse)
  })
_sym_db.RegisterMessage(GetFeatureFlagResponse)

DeleteFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('DeleteFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREFLAGREQUEST,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.DeleteFeatureFlagRequest)
  })
_sym_db.RegisterMessage(DeleteFeatureFlagRequest)

DeleteFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('DeleteFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREFLAGRESPONSE,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.DeleteFeatureFlagResponse)
  })
_sym_db.RegisterMessage(DeleteFeatureFlagResponse)

SetFeatureFlagForStationsRequest = _reflection.GeneratedProtocolMessageType('SetFeatureFlagForStationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGFORSTATIONSREQUEST,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.SetFeatureFlagForStationsRequest)
  })
_sym_db.RegisterMessage(SetFeatureFlagForStationsRequest)

SetFeatureFlagForStationsResponse = _reflection.GeneratedProtocolMessageType('SetFeatureFlagForStationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGFORSTATIONSRESPONSE,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.SetFeatureFlagForStationsResponse)
  })
_sym_db.RegisterMessage(SetFeatureFlagForStationsResponse)

IsFeatureFlagEnabledForStationsRequest = _reflection.GeneratedProtocolMessageType('IsFeatureFlagEnabledForStationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISFEATUREFLAGENABLEDFORSTATIONSREQUEST,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.IsFeatureFlagEnabledForStationsRequest)
  })
_sym_db.RegisterMessage(IsFeatureFlagEnabledForStationsRequest)

IsFeatureFlagEnabledForStationsResponse = _reflection.GeneratedProtocolMessageType('IsFeatureFlagEnabledForStationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISFEATUREFLAGENABLEDFORSTATIONSRESPONSE,
  '__module__' : 'FeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:featureflag.services.types.IsFeatureFlagEnabledForStationsResponse)
  })
_sym_db.RegisterMessage(IsFeatureFlagEnabledForStationsResponse)


DESCRIPTOR._options = None

_FEATUREFLAGSERVICE = _descriptor.ServiceDescriptor(
  name='FeatureFlagService',
  full_name='featureflag.services.types.FeatureFlagService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=977,
  serialized_end=1698,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeatureFlag',
    full_name='featureflag.services.types.FeatureFlagService.GetFeatureFlag',
    index=0,
    containing_service=None,
    input_type=_GETFEATUREFLAGREQUEST,
    output_type=_GETFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFeatureFlag',
    full_name='featureflag.services.types.FeatureFlagService.SetFeatureFlag',
    index=1,
    containing_service=None,
    input_type=_SETFEATUREFLAGREQUEST,
    output_type=_SETFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteFeatureFlag',
    full_name='featureflag.services.types.FeatureFlagService.DeleteFeatureFlag',
    index=2,
    containing_service=None,
    input_type=_DELETEFEATUREFLAGREQUEST,
    output_type=_DELETEFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFeatureFlagForStations',
    full_name='featureflag.services.types.FeatureFlagService.SetFeatureFlagForStations',
    index=3,
    containing_service=None,
    input_type=_SETFEATUREFLAGFORSTATIONSREQUEST,
    output_type=_SETFEATUREFLAGFORSTATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IsFeatureFlagEnabledForStations',
    full_name='featureflag.services.types.FeatureFlagService.IsFeatureFlagEnabledForStations',
    index=4,
    containing_service=None,
    input_type=_ISFEATUREFLAGENABLEDFORSTATIONSREQUEST,
    output_type=_ISFEATUREFLAGENABLEDFORSTATIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FEATUREFLAGSERVICE)

DESCRIPTOR.services_by_name['FeatureFlagService'] = _FEATUREFLAGSERVICE

# @@protoc_insertion_point(module_scope)
