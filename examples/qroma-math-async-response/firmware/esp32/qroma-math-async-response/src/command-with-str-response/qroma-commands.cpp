#include "qroma-commands.h"
#include "qroma-project.h"


void onHelloQroma(HelloQroma * message) {
  Serial.print("Hello ");
  Serial.println(message->name);
}

PbCommandProcessor<HelloQroma, HelloQroma_fields> helloQromaPbProcessor = PbCommandProcessor<HelloQroma, HelloQroma_fields>(onHelloQroma);
