# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gasstation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gasstation.proto',
  package='gasStation',
  syntax='proto3',
  serialized_options=_b('Z\ngasStation\222AN\022\037\n\030Gas Station data service2\0031.0\"\004/api*\001\0012\020application/json:\020application/json'),
  serialized_pb=_b('\n\x10gasstation.proto\x12\ngasStation\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\"Q\n\x0eResponseHeader\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.gasStation.ResponseStatus\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x10\n\x0eHealthzRequest\"=\n\x0fHealthzResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.gasStation.ResponseHeader\";\n\x03Gas\x12%\n\x08gas_type\x18\x01 \x01(\x0e\x32\x13.gasStation.GasType\x12\r\n\x05value\x18\x02 \x01(\t\"\x0c\n\nGasRequest\"W\n\x0bGasResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.gasStation.ResponseHeader\x12\x1c\n\x03gas\x18\x02 \x03(\x0b\x32\x0f.gasStation.Gas*J\n\x0eResponseStatus\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03*;\n\x07GasType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\x0b\n\x07\x41VERAGE\x10\x02\x12\x0c\n\x08SAFE_LOW\x10\x03\x32\xb4\x01\n\x11GasStationService\x12V\n\x07Healthz\x12\x1a.gasStation.HealthzRequest\x1a\x1b.gasStation.HealthzResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/health\x12G\n\x03Get\x12\x16.gasStation.GasRequest\x1a\x17.gasStation.GasResponse\"\x0f\x82\xd3\xe4\x93\x02\t\x12\x07/v1/gasB]Z\ngasStation\x92\x41N\x12\x1f\n\x18Gas Station data service2\x03\x31.0\"\x04/api*\x01\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])

_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='gasStation.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_SET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=469,
  serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS)

ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
_GASTYPE = _descriptor.EnumDescriptor(
  name='GasType',
  full_name='gasStation.GasType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVERAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFE_LOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=545,
  serialized_end=604,
)
_sym_db.RegisterEnumDescriptor(_GASTYPE)

GasType = enum_type_wrapper.EnumTypeWrapper(_GASTYPE)
NOT_SET = 0
SUCCESS = 1
ERROR = 2
INVALID_REQUEST = 3
UNKNOWN = 0
FAST = 1
AVERAGE = 2
SAFE_LOW = 3



_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='gasStation.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='gasStation.ResponseHeader.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='gasStation.ResponseHeader.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=141,
  serialized_end=222,
)


_HEALTHZREQUEST = _descriptor.Descriptor(
  name='HealthzRequest',
  full_name='gasStation.HealthzRequest',
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
  serialized_start=224,
  serialized_end=240,
)


_HEALTHZRESPONSE = _descriptor.Descriptor(
  name='HealthzResponse',
  full_name='gasStation.HealthzResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='gasStation.HealthzResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=242,
  serialized_end=303,
)


_GAS = _descriptor.Descriptor(
  name='Gas',
  full_name='gasStation.Gas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_type', full_name='gasStation.Gas.gas_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='gasStation.Gas.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=305,
  serialized_end=364,
)


_GASREQUEST = _descriptor.Descriptor(
  name='GasRequest',
  full_name='gasStation.GasRequest',
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
  serialized_start=366,
  serialized_end=378,
)


_GASRESPONSE = _descriptor.Descriptor(
  name='GasResponse',
  full_name='gasStation.GasResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='gasStation.GasResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas', full_name='gasStation.GasResponse.gas', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=380,
  serialized_end=467,
)

_RESPONSEHEADER.fields_by_name['status'].enum_type = _RESPONSESTATUS
_HEALTHZRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_GAS.fields_by_name['gas_type'].enum_type = _GASTYPE
_GASRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_GASRESPONSE.fields_by_name['gas'].message_type = _GAS
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['HealthzRequest'] = _HEALTHZREQUEST
DESCRIPTOR.message_types_by_name['HealthzResponse'] = _HEALTHZRESPONSE
DESCRIPTOR.message_types_by_name['Gas'] = _GAS
DESCRIPTOR.message_types_by_name['GasRequest'] = _GASREQUEST
DESCRIPTOR.message_types_by_name['GasResponse'] = _GASRESPONSE
DESCRIPTOR.enum_types_by_name['ResponseStatus'] = _RESPONSESTATUS
DESCRIPTOR.enum_types_by_name['GasType'] = _GASTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEHEADER,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.ResponseHeader)
  })
_sym_db.RegisterMessage(ResponseHeader)

HealthzRequest = _reflection.GeneratedProtocolMessageType('HealthzRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHZREQUEST,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.HealthzRequest)
  })
_sym_db.RegisterMessage(HealthzRequest)

HealthzResponse = _reflection.GeneratedProtocolMessageType('HealthzResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHZRESPONSE,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.HealthzResponse)
  })
_sym_db.RegisterMessage(HealthzResponse)

Gas = _reflection.GeneratedProtocolMessageType('Gas', (_message.Message,), {
  'DESCRIPTOR' : _GAS,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.Gas)
  })
_sym_db.RegisterMessage(Gas)

GasRequest = _reflection.GeneratedProtocolMessageType('GasRequest', (_message.Message,), {
  'DESCRIPTOR' : _GASREQUEST,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.GasRequest)
  })
_sym_db.RegisterMessage(GasRequest)

GasResponse = _reflection.GeneratedProtocolMessageType('GasResponse', (_message.Message,), {
  'DESCRIPTOR' : _GASRESPONSE,
  '__module__' : 'gasstation_pb2'
  # @@protoc_insertion_point(class_scope:gasStation.GasResponse)
  })
_sym_db.RegisterMessage(GasResponse)


DESCRIPTOR._options = None

_GASSTATIONSERVICE = _descriptor.ServiceDescriptor(
  name='GasStationService',
  full_name='gasStation.GasStationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=607,
  serialized_end=787,
  methods=[
  _descriptor.MethodDescriptor(
    name='Healthz',
    full_name='gasStation.GasStationService.Healthz',
    index=0,
    containing_service=None,
    input_type=_HEALTHZREQUEST,
    output_type=_HEALTHZRESPONSE,
    serialized_options=_b('\202\323\344\223\002\014\022\n/v1/health'),
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='gasStation.GasStationService.Get',
    index=1,
    containing_service=None,
    input_type=_GASREQUEST,
    output_type=_GASRESPONSE,
    serialized_options=_b('\202\323\344\223\002\t\022\007/v1/gas'),
  ),
])
_sym_db.RegisterServiceDescriptor(_GASSTATIONSERVICE)

DESCRIPTOR.services_by_name['GasStationService'] = _GASSTATIONSERVICE

# @@protoc_insertion_point(module_scope)
