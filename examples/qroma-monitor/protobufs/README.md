# Protocol Buffers for Embedded Device IO

## Getting Started

Qroma [uses Docker](https://www.docker.com/get-started/) for its Protocol Buffer build chain, so you will need to have it installed. See https://github.com/qromatech/docker-qromatech.

Once you have docker on your system and available on the command line, start defining your commands in `$PROJECT_ROOT/dev-io/protobufs/protofiles-in`.

Run the `docker-protobuf-compile` script for your platform. The script will take the contents of the `protofiles-in` directory and create the definition code for the default qroma languages in the `profofiles-out` directory.

Platform scripts are:
* Windows - `docker-protobuf-compile.bat`
* Mac - `docker-protobuf-compile.zsh`

## Rationale

Software developers spend a lot of time on getting computer languages and the programs build on them to have shared data types at the wire level. Protocol buffers are Google's solution to having one set of types that can be serialized and deserialized across multiple platforms. Protocol buffers are the default data-sharing mechanism for Qroma projects due to their power, flexibility, and support for lots of different development environments and styles.

The default languages Qroma supports out of the box are:
* C/C++
* TypeScript
* Python
* Dart
