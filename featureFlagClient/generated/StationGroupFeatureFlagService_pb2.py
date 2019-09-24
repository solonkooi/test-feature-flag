# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StationGroupFeatureFlagService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='StationGroupFeatureFlagService.proto',
  package='videa.featureflag.services.types.stationgroup',
  syntax='proto3',
  serialized_options=_b('\252\002-Videa.FeatureFlag.Services.Types.StationGroup\202\265\030\0051.0.0'),
  serialized_pb=_b('\n$StationGroupFeatureFlagService.proto\x12-videa.featureflag.services.types.stationgroup\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0btypes.proto\"\x83\x01\n\x15SetFeatureFlagRequest\x12!\n\x19station_group_external_id\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x04 \x01(\x08\"\x18\n\x16SetFeatureFlagResponse\"j\n\x15GetFeatureFlagRequest\x12!\n\x19station_group_external_id\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\"S\n\x16GetFeatureFlagResponse\x12 \n\x18\x66\x65\x61ture_flag_external_id\x18\x01 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x02 \x01(\x08\"\x8b\x01\n\x18\x44\x65leteFeatureFlagRequest\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12?\n\x19station_group_external_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x1b\n\x19\x44\x65leteFeatureFlagResponse\"\x94\x01\n%SetFeatureFlagForStationGroupsRequest\x12\"\n\x1astation_group_external_ids\x18\x01 \x03(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x03 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x04 \x01(\x08\"(\n&SetFeatureFlagForStationGroupsResponse2\xd9\x05\n\x1eStationGroupFeatureFlagService\x12\x9d\x01\n\x0eGetFeatureFlag\x12\x44.videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest\x1a\x45.videa.featureflag.services.types.stationgroup.GetFeatureFlagResponse\x12\x9d\x01\n\x0eSetFeatureFlag\x12\x44.videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest\x1a\x45.videa.featureflag.services.types.stationgroup.SetFeatureFlagResponse\x12\xa6\x01\n\x11\x44\x65leteFeatureFlag\x12G.videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest\x1aH.videa.featureflag.services.types.stationgroup.DeleteFeatureFlagResponse\x12\xcd\x01\n\x1eSetFeatureFlagForStationGroups\x12T.videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest\x1aU.videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsResponseB9\xaa\x02-Videa.FeatureFlag.Services.Types.StationGroup\x82\xb5\x18\x05\x31.0.0b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,types__pb2.DESCRIPTOR,])




_SETFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='SetFeatureFlagRequest',
  full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_group_external_id', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest.station_group_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest.feature_enabled', index=3,
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
  serialized_start=133,
  serialized_end=264,
)


_SETFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='SetFeatureFlagResponse',
  full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagResponse',
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
  serialized_start=266,
  serialized_end=290,
)


_GETFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='GetFeatureFlagRequest',
  full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_group_external_id', full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest.station_group_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=292,
  serialized_end=398,
)


_GETFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='GetFeatureFlagResponse',
  full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_flag_external_id', full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagResponse.feature_flag_external_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='videa.featureflag.services.types.stationgroup.GetFeatureFlagResponse.feature_enabled', index=1,
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
  serialized_start=400,
  serialized_end=483,
)


_DELETEFEATUREFLAGREQUEST = _descriptor.Descriptor(
  name='DeleteFeatureFlagRequest',
  full_name='videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest.feature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='station_group_external_id', full_name='videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest.station_group_external_id', index=2,
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
  serialized_start=486,
  serialized_end=625,
)


_DELETEFEATUREFLAGRESPONSE = _descriptor.Descriptor(
  name='DeleteFeatureFlagResponse',
  full_name='videa.featureflag.services.types.stationgroup.DeleteFeatureFlagResponse',
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
  serialized_start=627,
  serialized_end=654,
)


_SETFEATUREFLAGFORSTATIONGROUPSREQUEST = _descriptor.Descriptor(
  name='SetFeatureFlagForStationGroupsRequest',
  full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_group_external_ids', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest.station_group_external_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest.application_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest.feature_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest.feature_enabled', index=3,
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
  serialized_start=657,
  serialized_end=805,
)


_SETFEATUREFLAGFORSTATIONGROUPSRESPONSE = _descriptor.Descriptor(
  name='SetFeatureFlagForStationGroupsResponse',
  full_name='videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsResponse',
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
  serialized_start=807,
  serialized_end=847,
)

_DELETEFEATUREFLAGREQUEST.fields_by_name['station_group_external_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['SetFeatureFlagRequest'] = _SETFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['SetFeatureFlagResponse'] = _SETFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureFlagRequest'] = _GETFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['GetFeatureFlagResponse'] = _GETFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['DeleteFeatureFlagRequest'] = _DELETEFEATUREFLAGREQUEST
DESCRIPTOR.message_types_by_name['DeleteFeatureFlagResponse'] = _DELETEFEATUREFLAGRESPONSE
DESCRIPTOR.message_types_by_name['SetFeatureFlagForStationGroupsRequest'] = _SETFEATUREFLAGFORSTATIONGROUPSREQUEST
DESCRIPTOR.message_types_by_name['SetFeatureFlagForStationGroupsResponse'] = _SETFEATUREFLAGFORSTATIONGROUPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('SetFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGREQUEST,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.SetFeatureFlagRequest)
  })
_sym_db.RegisterMessage(SetFeatureFlagRequest)

SetFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('SetFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGRESPONSE,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.SetFeatureFlagResponse)
  })
_sym_db.RegisterMessage(SetFeatureFlagResponse)

GetFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('GetFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATUREFLAGREQUEST,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.GetFeatureFlagRequest)
  })
_sym_db.RegisterMessage(GetFeatureFlagRequest)

GetFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('GetFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEATUREFLAGRESPONSE,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.GetFeatureFlagResponse)
  })
_sym_db.RegisterMessage(GetFeatureFlagResponse)

DeleteFeatureFlagRequest = _reflection.GeneratedProtocolMessageType('DeleteFeatureFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREFLAGREQUEST,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.DeleteFeatureFlagRequest)
  })
_sym_db.RegisterMessage(DeleteFeatureFlagRequest)

DeleteFeatureFlagResponse = _reflection.GeneratedProtocolMessageType('DeleteFeatureFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFEATUREFLAGRESPONSE,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.DeleteFeatureFlagResponse)
  })
_sym_db.RegisterMessage(DeleteFeatureFlagResponse)

SetFeatureFlagForStationGroupsRequest = _reflection.GeneratedProtocolMessageType('SetFeatureFlagForStationGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGFORSTATIONGROUPSREQUEST,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsRequest)
  })
_sym_db.RegisterMessage(SetFeatureFlagForStationGroupsRequest)

SetFeatureFlagForStationGroupsResponse = _reflection.GeneratedProtocolMessageType('SetFeatureFlagForStationGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETFEATUREFLAGFORSTATIONGROUPSRESPONSE,
  '__module__' : 'StationGroupFeatureFlagService_pb2'
  # @@protoc_insertion_point(class_scope:videa.featureflag.services.types.stationgroup.SetFeatureFlagForStationGroupsResponse)
  })
_sym_db.RegisterMessage(SetFeatureFlagForStationGroupsResponse)


DESCRIPTOR._options = None

_STATIONGROUPFEATUREFLAGSERVICE = _descriptor.ServiceDescriptor(
  name='StationGroupFeatureFlagService',
  full_name='videa.featureflag.services.types.stationgroup.StationGroupFeatureFlagService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=850,
  serialized_end=1579,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeatureFlag',
    full_name='videa.featureflag.services.types.stationgroup.StationGroupFeatureFlagService.GetFeatureFlag',
    index=0,
    containing_service=None,
    input_type=_GETFEATUREFLAGREQUEST,
    output_type=_GETFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFeatureFlag',
    full_name='videa.featureflag.services.types.stationgroup.StationGroupFeatureFlagService.SetFeatureFlag',
    index=1,
    containing_service=None,
    input_type=_SETFEATUREFLAGREQUEST,
    output_type=_SETFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteFeatureFlag',
    full_name='videa.featureflag.services.types.stationgroup.StationGroupFeatureFlagService.DeleteFeatureFlag',
    index=2,
    containing_service=None,
    input_type=_DELETEFEATUREFLAGREQUEST,
    output_type=_DELETEFEATUREFLAGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFeatureFlagForStationGroups',
    full_name='videa.featureflag.services.types.stationgroup.StationGroupFeatureFlagService.SetFeatureFlagForStationGroups',
    index=3,
    containing_service=None,
    input_type=_SETFEATUREFLAGFORSTATIONGROUPSREQUEST,
    output_type=_SETFEATUREFLAGFORSTATIONGROUPSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATIONGROUPFEATUREFLAGSERVICE)

DESCRIPTOR.services_by_name['StationGroupFeatureFlagService'] = _STATIONGROUPFEATUREFLAGSERVICE

# @@protoc_insertion_point(module_scope)