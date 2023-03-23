#include "qroma-commands.h"
#include "qroma-project.h"


void onHelloQroma(HelloQroma * message) {
  qSerialPrint("Hello ");
  qSerialPrintln(message->name);
}

PbCommandProcessor<HelloQroma, HelloQroma_fields> helloQromaPbProcessor = PbCommandProcessor<HelloQroma, HelloQroma_fields>(onHelloQroma);
