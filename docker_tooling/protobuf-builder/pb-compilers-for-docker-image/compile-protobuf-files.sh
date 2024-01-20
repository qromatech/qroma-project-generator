#!/bin/bash

echo "Creating output directories"

mkdir outfiles
mkdir outfiles/proto
mkdir outfiles/nanopb
mkdir outfiles/python
mkdir outfiles/dart
mkdir outfiles/typescript
mkdir outfiles/javascript

echo "Copying out protobuf files"
cp -r /usr/src/app/protofiles/* outfiles/proto

echo "Compiling protobuf files"

cd /usr/src/app/protofiles
../generator/generator-bin/protoc *.proto --plugin=protoc-gen-dart=/root/.pub-cache/bin/protoc-gen-dart --nanopb_out=../outfiles/nanopb --python_out=../outfiles/python --dart_out=../outfiles/dart 


echo "Ignoring JS protobuf files"
# echo "Compiling JS protobuf files"
# npx protoc --proto_path /usr/src/app/protofiles /usr/src/app/protofiles/*.proto \
#       --js_out=import_style=commonjs,binary:../outfiles/javascript


echo "Compiling TS protobuf files"
npx protoc --ts_out ../outfiles/typescript \
      --proto_path /usr/src/app/protofiles \
      /usr/src/app/protofiles/*.proto \
      --experimental_allow_proto3_optional \
      --ts_opt use_proto_field_name \
      --ts_opt generate_dependencies


echo "Protobuf files compiled/generated by 'docker-protobuf-compile' using docker image qroma-project-generator-tools on " $(date) >> ../outfiles/compiled-by-qroma.txt
