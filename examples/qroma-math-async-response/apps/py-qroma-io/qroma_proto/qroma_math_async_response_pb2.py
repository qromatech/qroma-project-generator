# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qroma-math-async-response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='qroma-math-async-response.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fqroma-math-async-response.proto\"?\n\x0bMathProblem\x12\t\n\x01\x61\x18\x01 \x01(\r\x12\t\n\x01\x62\x18\x02 \x01(\r\x12\x1a\n\x02op\x18\x03 \x01(\x0e\x32\x0e.MathOperation\" \n\x0eMathResult_Add\x12\x0e\n\x06result\x18\x01 \x01(\r\"%\n\x13MathResult_Subtract\x12\x0e\n\x06result\x18\x01 \x01(\r\"F\n\x19MathResult_AddAndSubtract\x12\x11\n\taddResult\x18\x01 \x01(\r\x12\x16\n\x0esubtractResult\x18\x02 \x01(\r\"\xb3\x01\n\x13MathProblemResponse\x12$\n\taddResult\x18\x01 \x01(\x0b\x32\x0f.MathResult_AddH\x00\x12.\n\x0esubtractResult\x18\x02 \x01(\x0b\x32\x14.MathResult_SubtractH\x00\x12:\n\x14\x61\x64\x64\x41ndSubtractResult\x18\x03 \x01(\x0b\x32\x1a.MathResult_AddAndSubtractH\x00\x42\n\n\x08response*d\n\rMathOperation\x12\x11\n\rMathOp_NotSet\x10\x00\x12\x0e\n\nMathOp_Add\x10\x01\x12\x13\n\x0fMathOp_Subtract\x10\x02\x12\x1b\n\x17MathOp_Add_And_Subtract\x10\x03\x62\x06proto3'
)

_MATHOPERATION = _descriptor.EnumDescriptor(
  name='MathOperation',
  full_name='MathOperation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MathOp_NotSet', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MathOp_Add', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MathOp_Subtract', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MathOp_Add_And_Subtract', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=427,
  serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_MATHOPERATION)

MathOperation = enum_type_wrapper.EnumTypeWrapper(_MATHOPERATION)
MathOp_NotSet = 0
MathOp_Add = 1
MathOp_Subtract = 2
MathOp_Add_And_Subtract = 3



_MATHPROBLEM = _descriptor.Descriptor(
  name='MathProblem',
  full_name='MathProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='MathProblem.a', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='MathProblem.b', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='op', full_name='MathProblem.op', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=98,
)


_MATHRESULT_ADD = _descriptor.Descriptor(
  name='MathResult_Add',
  full_name='MathResult_Add',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='MathResult_Add.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=100,
  serialized_end=132,
)


_MATHRESULT_SUBTRACT = _descriptor.Descriptor(
  name='MathResult_Subtract',
  full_name='MathResult_Subtract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='MathResult_Subtract.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=134,
  serialized_end=171,
)


_MATHRESULT_ADDANDSUBTRACT = _descriptor.Descriptor(
  name='MathResult_AddAndSubtract',
  full_name='MathResult_AddAndSubtract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addResult', full_name='MathResult_AddAndSubtract.addResult', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtractResult', full_name='MathResult_AddAndSubtract.subtractResult', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=173,
  serialized_end=243,
)


_MATHPROBLEMRESPONSE = _descriptor.Descriptor(
  name='MathProblemResponse',
  full_name='MathProblemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addResult', full_name='MathProblemResponse.addResult', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtractResult', full_name='MathProblemResponse.subtractResult', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addAndSubtractResult', full_name='MathProblemResponse.addAndSubtractResult', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='response', full_name='MathProblemResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=246,
  serialized_end=425,
)

_MATHPROBLEM.fields_by_name['op'].enum_type = _MATHOPERATION
_MATHPROBLEMRESPONSE.fields_by_name['addResult'].message_type = _MATHRESULT_ADD
_MATHPROBLEMRESPONSE.fields_by_name['subtractResult'].message_type = _MATHRESULT_SUBTRACT
_MATHPROBLEMRESPONSE.fields_by_name['addAndSubtractResult'].message_type = _MATHRESULT_ADDANDSUBTRACT
_MATHPROBLEMRESPONSE.oneofs_by_name['response'].fields.append(
  _MATHPROBLEMRESPONSE.fields_by_name['addResult'])
_MATHPROBLEMRESPONSE.fields_by_name['addResult'].containing_oneof = _MATHPROBLEMRESPONSE.oneofs_by_name['response']
_MATHPROBLEMRESPONSE.oneofs_by_name['response'].fields.append(
  _MATHPROBLEMRESPONSE.fields_by_name['subtractResult'])
_MATHPROBLEMRESPONSE.fields_by_name['subtractResult'].containing_oneof = _MATHPROBLEMRESPONSE.oneofs_by_name['response']
_MATHPROBLEMRESPONSE.oneofs_by_name['response'].fields.append(
  _MATHPROBLEMRESPONSE.fields_by_name['addAndSubtractResult'])
_MATHPROBLEMRESPONSE.fields_by_name['addAndSubtractResult'].containing_oneof = _MATHPROBLEMRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['MathProblem'] = _MATHPROBLEM
DESCRIPTOR.message_types_by_name['MathResult_Add'] = _MATHRESULT_ADD
DESCRIPTOR.message_types_by_name['MathResult_Subtract'] = _MATHRESULT_SUBTRACT
DESCRIPTOR.message_types_by_name['MathResult_AddAndSubtract'] = _MATHRESULT_ADDANDSUBTRACT
DESCRIPTOR.message_types_by_name['MathProblemResponse'] = _MATHPROBLEMRESPONSE
DESCRIPTOR.enum_types_by_name['MathOperation'] = _MATHOPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MathProblem = _reflection.GeneratedProtocolMessageType('MathProblem', (_message.Message,), {
  'DESCRIPTOR' : _MATHPROBLEM,
  '__module__' : 'qroma_math_async_response_pb2'
  # @@protoc_insertion_point(class_scope:MathProblem)
  })
_sym_db.RegisterMessage(MathProblem)

MathResult_Add = _reflection.GeneratedProtocolMessageType('MathResult_Add', (_message.Message,), {
  'DESCRIPTOR' : _MATHRESULT_ADD,
  '__module__' : 'qroma_math_async_response_pb2'
  # @@protoc_insertion_point(class_scope:MathResult_Add)
  })
_sym_db.RegisterMessage(MathResult_Add)

MathResult_Subtract = _reflection.GeneratedProtocolMessageType('MathResult_Subtract', (_message.Message,), {
  'DESCRIPTOR' : _MATHRESULT_SUBTRACT,
  '__module__' : 'qroma_math_async_response_pb2'
  # @@protoc_insertion_point(class_scope:MathResult_Subtract)
  })
_sym_db.RegisterMessage(MathResult_Subtract)

MathResult_AddAndSubtract = _reflection.GeneratedProtocolMessageType('MathResult_AddAndSubtract', (_message.Message,), {
  'DESCRIPTOR' : _MATHRESULT_ADDANDSUBTRACT,
  '__module__' : 'qroma_math_async_response_pb2'
  # @@protoc_insertion_point(class_scope:MathResult_AddAndSubtract)
  })
_sym_db.RegisterMessage(MathResult_AddAndSubtract)

MathProblemResponse = _reflection.GeneratedProtocolMessageType('MathProblemResponse', (_message.Message,), {
  'DESCRIPTOR' : _MATHPROBLEMRESPONSE,
  '__module__' : 'qroma_math_async_response_pb2'
  # @@protoc_insertion_point(class_scope:MathProblemResponse)
  })
_sym_db.RegisterMessage(MathProblemResponse)


# @@protoc_insertion_point(module_scope)
