# FROM ubuntu:18.04 as builder
FROM ubuntu:22.04 as builder

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y python3 curl nano bash nodejs npm wget


ARG NANOPB_VERSION=0.4.8
ENV nanopb=nanopb-${NANOPB_VERSION}-linux-x86
ENV file=${nanopb}.tar.gz

ENV DART_VERSION=2.13.14
ENV DART_PROTOBUF_VERSION=2.0.0
ENV PROTOC_GEN_DART_VERSION=2.0.1


RUN curl -O https://jpa.kapsi.fi/nanopb/download/${file} && tar -xzf ${file}
RUN mkdir generator && cp -a ${nanopb}/. generator


# There are issues with building building/installing dart with docker on OSX
RUN apt-get install -y apt-transport-https
RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/dart.gpg
RUN echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | tee /etc/apt/sources.list.d/dart_stable.list
RUN apt-get update
RUN apt-get install dart

RUN dart pub global activate protoc_plugin


WORKDIR /usr/src/app

# RUN npm install protoc ts-protoc-gen
RUN npm install @protobuf-ts/protoc @protobuf-ts/plugin

# @protobuf-ts will try to download protoc if it's not already in place
RUN npx protoc || true


COPY pb-compilers-for-docker-image/compile-protobuf-files.sh .
# COPY ts-compile-ts-protobuf-files.sh .

CMD [ "./compile-protobuf-files.sh" ]
# CMD [ "./compile-ts-protobuf-files.sh" ]
#RUN [ "/usr/bin/bash" ]

