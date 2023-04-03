#ifndef QROMA_PROJECT_CONFIG_H
#define QROMA_PROJECT_CONFIG_H

#include "../qroma-proto/hello-qroma-with-pb-response.pb.h"

void onHelloQroma(HelloQroma * message, HelloQromaResponse * hqr);

// extern PbCommandWithResponseProcessor<HelloQroma, HelloQroma_fields, HelloQromaResponse, HelloQromaResponse_fields> helloQromaPbProcessor;

#endif
