# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallets.proto

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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wallets.proto',
  package='wallets',
  syntax='proto3',
  serialized_options=_b('Z\006wlt-go\222AH\022\026\n\017Wallets service2\0031.0\"\007/api/v1*\001\0012\020application/json:\020application/json'),
  serialized_pb=_b('\n\rwallets.proto\x12\x07wallets\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\"N\n\x0eResponseHeader\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.wallets.ResponseStatus\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x10\n\x0eHealthzRequest\":\n\x0fHealthzResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"f\n\x06Wallet\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x15\n\rcurrency_slug\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x13\n\x0bis_platform\x18\x04 \x01(\x08\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\x03\"4\n\x11MonitoringRequest\x12\x1f\n\x06wallet\x18\x01 \x01(\x0b\x32\x0f.wallets.Wallet\"=\n\x12MonitoringResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"A\n\x13\x43heckBalanceRequest\x12\x15\n\rbody_currency\x18\x01 \x01(\t\x12\x13\n\x0b\x62ody_amount\x18\x02 \x01(\t\"?\n\x14\x43heckBalanceResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"\xc5\x01\n\x0bTransaction\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t\x12\x11\n\twallet_id\x18\x06 \x01(\x03\x12\x14\n\x0c\x63urrencySlug\x18\x07 \x01(\t\x12*\n\x06status\x18\x08 \x01(\x0e\x32\x1a.wallets.TransactionStatus\x12\x12\n\nis_fee_trx\x18\t \x01(\x08\x12\x16\n\x0etime_confirmed\x18\n \x01(\x03\"?\n\x12TransactionRequest\x12)\n\x0btransaction\x18\x01 \x03(\x0b\x32\x14.wallets.Transaction\">\n\x13TransactionResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\"i\n\x18InputTransactionsRequest\x12\x11\n\twallet_id\x18\x01 \x01(\x03\x12\x16\n\x0ewallet_address\x18\x02 \x01(\t\x12\x11\n\ttime_from\x18\x03 \x01(\x03\x12\x0f\n\x07time_to\x18\x04 \x01(\x03\"p\n\x19InputTransactionsResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader\x12*\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x14.wallets.Transaction\"\xa5\x01\n\x1cPlatformWLTMonitoringRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x18\n\x10\x65xpected_address\x18\x02 \x01(\t\x12\x17\n\x0f\x65xpected_amount\x18\x03 \x01(\t\x12\x11\n\twallet_id\x18\x04 \x01(\x03\x12\x16\n\x0ewallet_address\x18\x05 \x01(\t\x12\x19\n\x11\x65xpected_currency\x18\x06 \x01(\t\"H\n\x1dPlatformWLTMonitoringResponse\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.wallets.ResponseHeader*J\n\x0eResponseStatus\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03*r\n\x11TransactionStatus\x12\r\n\tUNDEFINED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x12\x0e\n\nSUCCESSFUL\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07PENDING\x10\x05\x12\r\n\tCONFIRMED\x10\x06\x32\x84\x0b\n\x07Wallets\x12\x9d\x01\n\x07Healthz\x12\x17.wallets.HealthzRequest\x1a\x18.wallets.HealthzResponse\"_\x82\xd3\xe4\x93\x02\t\x12\x07/health\x92\x41M\x12\x18Health checking endpoint\x1a\x31Health checking endpoint. Returns HealthzResponse\x12\xd1\x01\n\x0fStartMonitoring\x12\x1a.wallets.MonitoringRequest\x1a\x1b.wallets.MonitoringResponse\"\x84\x01\x82\xd3\xe4\x93\x02\x16\"\x11/start_monitoring:\x01*\x92\x41\x65\x12+Start monitoring wallet on service endpoint\x1a\x36Send wallet with params to start monitoring on service\x12\xcd\x01\n\x0eStopMonitoring\x12\x1a.wallets.MonitoringRequest\x1a\x1b.wallets.MonitoringResponse\"\x81\x01\x82\xd3\xe4\x93\x02\x15\"\x10/stop_monitoring:\x01*\x92\x41\x63\x12*Stop monitoring wallet on service endpoint\x1a\x35Send wallet with params to stop monitoring on service\x12\xbb\x01\n\x0c\x43heckBalance\x12\x1c.wallets.CheckBalanceRequest\x1a\x1d.wallets.CheckBalanceResponse\"n\x82\xd3\xe4\x93\x02\x10\x12\x0e/check_balance\x92\x41U\x12\x31\x43heck Balance of platform wallets when issue loan\x1a Check balance when we issue loan\x12\xad\x01\n\tUpdateTrx\x12\x1b.wallets.TransactionRequest\x1a\x1c.wallets.TransactionResponse\"e\x82\xd3\xe4\x93\x02\x10\"\x0b/update_trx:\x01*\x92\x41L\x12\x1e\x45ndpoint to update transaction\x1a*Update status transactions from blockchain\x12\xce\x01\n\x14GetInputTransactions\x12!.wallets.InputTransactionsRequest\x1a\".wallets.InputTransactionsResponse\"o\x82\xd3\xe4\x93\x02\x10\x12\x0e/get_input_trx\x92\x41V\x12)Endpoint to get wallet input transactions\x1a)Endpoint to get wallet input transactions\x12\xf5\x01\n\x1dStartMonitoringPlatformWallet\x12%.wallets.PlatformWLTMonitoringRequest\x1a&.wallets.PlatformWLTMonitoringResponse\"\x84\x01\x82\xd3\xe4\x93\x02\x1f\"\x1a/start_monitoring/platform:\x01*\x92\x41\\\x12,Endpoint to start monitoring platform wallet\x1a,Endpoint to start monitoring platform walletBSZ\x06wlt-go\x92\x41H\x12\x16\n\x0fWallets service2\x03\x31.0\"\x07/api/v1*\x01\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])

_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='wallets.ResponseStatus',
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
  serialized_start=1470,
  serialized_end=1544,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS)

ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='wallets.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESSFUL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1546,
  serialized_end=1660,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
NOT_SET = 0
SUCCESS = 1
ERROR = 2
INVALID_REQUEST = 3
UNDEFINED = 0
NEW = 1
NOT_FOUND = 2
SUCCESSFUL = 3
FAILED = 4
PENDING = 5
CONFIRMED = 6



_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='wallets.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wallets.ResponseHeader.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='wallets.ResponseHeader.description', index=1,
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
  serialized_start=167,
  serialized_end=245,
)


_HEALTHZREQUEST = _descriptor.Descriptor(
  name='HealthzRequest',
  full_name='wallets.HealthzRequest',
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
  serialized_start=247,
  serialized_end=263,
)


_HEALTHZRESPONSE = _descriptor.Descriptor(
  name='HealthzResponse',
  full_name='wallets.HealthzResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.HealthzResponse.header', index=0,
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
  serialized_start=265,
  serialized_end=323,
)


_WALLET = _descriptor.Descriptor(
  name='Wallet',
  full_name='wallets.Wallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wallets.Wallet.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_slug', full_name='wallets.Wallet.currency_slug', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='wallets.Wallet.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_platform', full_name='wallets.Wallet.is_platform', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='wallets.Wallet.external_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=325,
  serialized_end=427,
)


_MONITORINGREQUEST = _descriptor.Descriptor(
  name='MonitoringRequest',
  full_name='wallets.MonitoringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet', full_name='wallets.MonitoringRequest.wallet', index=0,
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
  serialized_start=429,
  serialized_end=481,
)


_MONITORINGRESPONSE = _descriptor.Descriptor(
  name='MonitoringResponse',
  full_name='wallets.MonitoringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.MonitoringResponse.header', index=0,
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
  serialized_start=483,
  serialized_end=544,
)


_CHECKBALANCEREQUEST = _descriptor.Descriptor(
  name='CheckBalanceRequest',
  full_name='wallets.CheckBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body_currency', full_name='wallets.CheckBalanceRequest.body_currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body_amount', full_name='wallets.CheckBalanceRequest.body_amount', index=1,
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
  serialized_start=546,
  serialized_end=611,
)


_CHECKBALANCERESPONSE = _descriptor.Descriptor(
  name='CheckBalanceResponse',
  full_name='wallets.CheckBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.CheckBalanceResponse.header', index=0,
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
  serialized_start=613,
  serialized_end=676,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='wallets.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='wallets.Transaction.from', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='wallets.Transaction.to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='wallets.Transaction.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='wallets.Transaction.value', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wallet_id', full_name='wallets.Transaction.wallet_id', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currencySlug', full_name='wallets.Transaction.currencySlug', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='wallets.Transaction.status', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_fee_trx', full_name='wallets.Transaction.is_fee_trx', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_confirmed', full_name='wallets.Transaction.time_confirmed', index=8,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=679,
  serialized_end=876,
)


_TRANSACTIONREQUEST = _descriptor.Descriptor(
  name='TransactionRequest',
  full_name='wallets.TransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='wallets.TransactionRequest.transaction', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=878,
  serialized_end=941,
)


_TRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='TransactionResponse',
  full_name='wallets.TransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.TransactionResponse.header', index=0,
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
  serialized_start=943,
  serialized_end=1005,
)


_INPUTTRANSACTIONSREQUEST = _descriptor.Descriptor(
  name='InputTransactionsRequest',
  full_name='wallets.InputTransactionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet_id', full_name='wallets.InputTransactionsRequest.wallet_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wallet_address', full_name='wallets.InputTransactionsRequest.wallet_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_from', full_name='wallets.InputTransactionsRequest.time_from', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to', full_name='wallets.InputTransactionsRequest.time_to', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1007,
  serialized_end=1112,
)


_INPUTTRANSACTIONSRESPONSE = _descriptor.Descriptor(
  name='InputTransactionsResponse',
  full_name='wallets.InputTransactionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.InputTransactionsResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='wallets.InputTransactionsResponse.transactions', index=1,
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
  serialized_start=1114,
  serialized_end=1226,
)


_PLATFORMWLTMONITORINGREQUEST = _descriptor.Descriptor(
  name='PlatformWLTMonitoringRequest',
  full_name='wallets.PlatformWLTMonitoringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wallets.PlatformWLTMonitoringRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_address', full_name='wallets.PlatformWLTMonitoringRequest.expected_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_amount', full_name='wallets.PlatformWLTMonitoringRequest.expected_amount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wallet_id', full_name='wallets.PlatformWLTMonitoringRequest.wallet_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wallet_address', full_name='wallets.PlatformWLTMonitoringRequest.wallet_address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_currency', full_name='wallets.PlatformWLTMonitoringRequest.expected_currency', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1229,
  serialized_end=1394,
)


_PLATFORMWLTMONITORINGRESPONSE = _descriptor.Descriptor(
  name='PlatformWLTMonitoringResponse',
  full_name='wallets.PlatformWLTMonitoringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='wallets.PlatformWLTMonitoringResponse.header', index=0,
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
  serialized_start=1396,
  serialized_end=1468,
)

_RESPONSEHEADER.fields_by_name['status'].enum_type = _RESPONSESTATUS
_HEALTHZRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_MONITORINGREQUEST.fields_by_name['wallet'].message_type = _WALLET
_MONITORINGRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_CHECKBALANCERESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_TRANSACTION.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTIONREQUEST.fields_by_name['transaction'].message_type = _TRANSACTION
_TRANSACTIONRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_INPUTTRANSACTIONSRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_INPUTTRANSACTIONSRESPONSE.fields_by_name['transactions'].message_type = _TRANSACTION
_PLATFORMWLTMONITORINGRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['HealthzRequest'] = _HEALTHZREQUEST
DESCRIPTOR.message_types_by_name['HealthzResponse'] = _HEALTHZRESPONSE
DESCRIPTOR.message_types_by_name['Wallet'] = _WALLET
DESCRIPTOR.message_types_by_name['MonitoringRequest'] = _MONITORINGREQUEST
DESCRIPTOR.message_types_by_name['MonitoringResponse'] = _MONITORINGRESPONSE
DESCRIPTOR.message_types_by_name['CheckBalanceRequest'] = _CHECKBALANCEREQUEST
DESCRIPTOR.message_types_by_name['CheckBalanceResponse'] = _CHECKBALANCERESPONSE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionRequest'] = _TRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['TransactionResponse'] = _TRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['InputTransactionsRequest'] = _INPUTTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name['InputTransactionsResponse'] = _INPUTTRANSACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['PlatformWLTMonitoringRequest'] = _PLATFORMWLTMONITORINGREQUEST
DESCRIPTOR.message_types_by_name['PlatformWLTMonitoringResponse'] = _PLATFORMWLTMONITORINGRESPONSE
DESCRIPTOR.enum_types_by_name['ResponseStatus'] = _RESPONSESTATUS
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEHEADER,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.ResponseHeader)
  })
_sym_db.RegisterMessage(ResponseHeader)

HealthzRequest = _reflection.GeneratedProtocolMessageType('HealthzRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHZREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.HealthzRequest)
  })
_sym_db.RegisterMessage(HealthzRequest)

HealthzResponse = _reflection.GeneratedProtocolMessageType('HealthzResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHZRESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.HealthzResponse)
  })
_sym_db.RegisterMessage(HealthzResponse)

Wallet = _reflection.GeneratedProtocolMessageType('Wallet', (_message.Message,), {
  'DESCRIPTOR' : _WALLET,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.Wallet)
  })
_sym_db.RegisterMessage(Wallet)

MonitoringRequest = _reflection.GeneratedProtocolMessageType('MonitoringRequest', (_message.Message,), {
  'DESCRIPTOR' : _MONITORINGREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.MonitoringRequest)
  })
_sym_db.RegisterMessage(MonitoringRequest)

MonitoringResponse = _reflection.GeneratedProtocolMessageType('MonitoringResponse', (_message.Message,), {
  'DESCRIPTOR' : _MONITORINGRESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.MonitoringResponse)
  })
_sym_db.RegisterMessage(MonitoringResponse)

CheckBalanceRequest = _reflection.GeneratedProtocolMessageType('CheckBalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKBALANCEREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.CheckBalanceRequest)
  })
_sym_db.RegisterMessage(CheckBalanceRequest)

CheckBalanceResponse = _reflection.GeneratedProtocolMessageType('CheckBalanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKBALANCERESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.CheckBalanceResponse)
  })
_sym_db.RegisterMessage(CheckBalanceResponse)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

TransactionRequest = _reflection.GeneratedProtocolMessageType('TransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.TransactionRequest)
  })
_sym_db.RegisterMessage(TransactionRequest)

TransactionResponse = _reflection.GeneratedProtocolMessageType('TransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.TransactionResponse)
  })
_sym_db.RegisterMessage(TransactionResponse)

InputTransactionsRequest = _reflection.GeneratedProtocolMessageType('InputTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _INPUTTRANSACTIONSREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.InputTransactionsRequest)
  })
_sym_db.RegisterMessage(InputTransactionsRequest)

InputTransactionsResponse = _reflection.GeneratedProtocolMessageType('InputTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _INPUTTRANSACTIONSRESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.InputTransactionsResponse)
  })
_sym_db.RegisterMessage(InputTransactionsResponse)

PlatformWLTMonitoringRequest = _reflection.GeneratedProtocolMessageType('PlatformWLTMonitoringRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLATFORMWLTMONITORINGREQUEST,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.PlatformWLTMonitoringRequest)
  })
_sym_db.RegisterMessage(PlatformWLTMonitoringRequest)

PlatformWLTMonitoringResponse = _reflection.GeneratedProtocolMessageType('PlatformWLTMonitoringResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLATFORMWLTMONITORINGRESPONSE,
  '__module__' : 'wallets_pb2'
  # @@protoc_insertion_point(class_scope:wallets.PlatformWLTMonitoringResponse)
  })
_sym_db.RegisterMessage(PlatformWLTMonitoringResponse)


DESCRIPTOR._options = None

_WALLETS = _descriptor.ServiceDescriptor(
  name='Wallets',
  full_name='wallets.Wallets',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1663,
  serialized_end=3075,
  methods=[
  _descriptor.MethodDescriptor(
    name='Healthz',
    full_name='wallets.Wallets.Healthz',
    index=0,
    containing_service=None,
    input_type=_HEALTHZREQUEST,
    output_type=_HEALTHZRESPONSE,
    serialized_options=_b('\202\323\344\223\002\t\022\007/health\222AM\022\030Health checking endpoint\0321Health checking endpoint. Returns HealthzResponse'),
  ),
  _descriptor.MethodDescriptor(
    name='StartMonitoring',
    full_name='wallets.Wallets.StartMonitoring',
    index=1,
    containing_service=None,
    input_type=_MONITORINGREQUEST,
    output_type=_MONITORINGRESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\"\021/start_monitoring:\001*\222Ae\022+Start monitoring wallet on service endpoint\0326Send wallet with params to start monitoring on service'),
  ),
  _descriptor.MethodDescriptor(
    name='StopMonitoring',
    full_name='wallets.Wallets.StopMonitoring',
    index=2,
    containing_service=None,
    input_type=_MONITORINGREQUEST,
    output_type=_MONITORINGRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\020/stop_monitoring:\001*\222Ac\022*Stop monitoring wallet on service endpoint\0325Send wallet with params to stop monitoring on service'),
  ),
  _descriptor.MethodDescriptor(
    name='CheckBalance',
    full_name='wallets.Wallets.CheckBalance',
    index=3,
    containing_service=None,
    input_type=_CHECKBALANCEREQUEST,
    output_type=_CHECKBALANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/check_balance\222AU\0221Check Balance of platform wallets when issue loan\032 Check balance when we issue loan'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTrx',
    full_name='wallets.Wallets.UpdateTrx',
    index=4,
    containing_service=None,
    input_type=_TRANSACTIONREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\"\013/update_trx:\001*\222AL\022\036Endpoint to update transaction\032*Update status transactions from blockchain'),
  ),
  _descriptor.MethodDescriptor(
    name='GetInputTransactions',
    full_name='wallets.Wallets.GetInputTransactions',
    index=5,
    containing_service=None,
    input_type=_INPUTTRANSACTIONSREQUEST,
    output_type=_INPUTTRANSACTIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/get_input_trx\222AV\022)Endpoint to get wallet input transactions\032)Endpoint to get wallet input transactions'),
  ),
  _descriptor.MethodDescriptor(
    name='StartMonitoringPlatformWallet',
    full_name='wallets.Wallets.StartMonitoringPlatformWallet',
    index=6,
    containing_service=None,
    input_type=_PLATFORMWLTMONITORINGREQUEST,
    output_type=_PLATFORMWLTMONITORINGRESPONSE,
    serialized_options=_b('\202\323\344\223\002\037\"\032/start_monitoring/platform:\001*\222A\\\022,Endpoint to start monitoring platform wallet\032,Endpoint to start monitoring platform wallet'),
  ),
])
_sym_db.RegisterServiceDescriptor(_WALLETS)

DESCRIPTOR.services_by_name['Wallets'] = _WALLETS

# @@protoc_insertion_point(module_scope)
