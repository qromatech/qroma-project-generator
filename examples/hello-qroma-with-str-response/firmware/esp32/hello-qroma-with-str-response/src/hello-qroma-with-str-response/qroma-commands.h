#ifndef QROMA_PROJECT_CONFIG_H
#define QROMA_PROJECT_CONFIG_H

#include "qroma/qroma.h"
#include "../qroma-proto/hello-qroma-with-str-response.pb.h"

extern PbCommandProcessor<HelloQroma, HelloQroma_fields> helloQromaPbProcessor;

#endif
