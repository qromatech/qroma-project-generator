#include "../qroma-proto/hello-qroma-with-pb-response.pb.h"

uint32_t helloQromaCallCount = 0;


void onHelloQroma(HelloQroma * message, HelloQromaResponse * hqr) {
  helloQromaCallCount++;

  hqr->response[0] = 0;
  strncat(hqr->response, "Hello qroma: ", sizeof(HelloQromaResponse::response));
  strncat(hqr->response, message->name, sizeof(HelloQroma::name));

  hqr->callCount = helloQromaCallCount;
  hqr->nameLength = strnlen(message->name, sizeof(HelloQroma::name));
}
