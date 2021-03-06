# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommender.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recommender.proto',
  package='pb',
  syntax='proto3',
  serialized_options=_b('\n(edu.beuth.movies.services.recommender.pb'),
  serialized_pb=_b('\n\x11recommender.proto\x12\x02pb\"2\n\x16RecommendMoviesRequest\x12\x18\n\x10reference_movies\x18\x01 \x03(\t\"5\n\x17RecommendMoviesResponse\x12\x1a\n\x12recommended_movies\x18\x01 \x03(\t2_\n\x10MovieRecommender\x12K\n\x10recommend_movies\x12\x1a.pb.RecommendMoviesRequest\x1a\x1b.pb.RecommendMoviesResponseB*\n(edu.beuth.movies.services.recommender.pbb\x06proto3')
)




_RECOMMENDMOVIESREQUEST = _descriptor.Descriptor(
  name='RecommendMoviesRequest',
  full_name='pb.RecommendMoviesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_movies', full_name='pb.RecommendMoviesRequest.reference_movies', index=0,
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
  serialized_start=25,
  serialized_end=75,
)


_RECOMMENDMOVIESRESPONSE = _descriptor.Descriptor(
  name='RecommendMoviesResponse',
  full_name='pb.RecommendMoviesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recommended_movies', full_name='pb.RecommendMoviesResponse.recommended_movies', index=0,
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
  serialized_start=77,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['RecommendMoviesRequest'] = _RECOMMENDMOVIESREQUEST
DESCRIPTOR.message_types_by_name['RecommendMoviesResponse'] = _RECOMMENDMOVIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendMoviesRequest = _reflection.GeneratedProtocolMessageType('RecommendMoviesRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDMOVIESREQUEST,
  __module__ = 'recommender_pb2'
  # @@protoc_insertion_point(class_scope:pb.RecommendMoviesRequest)
  ))
_sym_db.RegisterMessage(RecommendMoviesRequest)

RecommendMoviesResponse = _reflection.GeneratedProtocolMessageType('RecommendMoviesResponse', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDMOVIESRESPONSE,
  __module__ = 'recommender_pb2'
  # @@protoc_insertion_point(class_scope:pb.RecommendMoviesResponse)
  ))
_sym_db.RegisterMessage(RecommendMoviesResponse)


DESCRIPTOR._options = None

_MOVIERECOMMENDER = _descriptor.ServiceDescriptor(
  name='MovieRecommender',
  full_name='pb.MovieRecommender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=132,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='recommend_movies',
    full_name='pb.MovieRecommender.recommend_movies',
    index=0,
    containing_service=None,
    input_type=_RECOMMENDMOVIESREQUEST,
    output_type=_RECOMMENDMOVIESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOVIERECOMMENDER)

DESCRIPTOR.services_by_name['MovieRecommender'] = _MOVIERECOMMENDER

# @@protoc_insertion_point(module_scope)
