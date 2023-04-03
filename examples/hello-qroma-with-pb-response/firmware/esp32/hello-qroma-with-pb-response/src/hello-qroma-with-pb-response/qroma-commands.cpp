#include "qroma-commands.h"
#include "qroma-project.h"

uint32_t helloQromaCallCount = 0;

void onHelloQroma(HelloQroma * message, HelloQromaResponse * hqr) {
  helloQromaCallCount++;

  strncat(hqr->response, "Hello qroma: ", sizeof(HelloQromaResponse::response));
  strncat(hqr->response, message->name, sizeof(HelloQroma::name));
  hqr->callCount = helloQromaCallCount;
  hqr->nameLength = strnlen(message->name, sizeof(HelloQroma::name));
}


PbCommandWithResponseProcessor<HelloQroma, HelloQroma_fields, HelloQromaResponse, HelloQromaResponse_fields> helloQromaPbProcessor = 
  PbCommandWithResponseProcessor<HelloQroma, HelloQroma_fields, HelloQromaResponse, HelloQromaResponse_fields>(onHelloQroma);
