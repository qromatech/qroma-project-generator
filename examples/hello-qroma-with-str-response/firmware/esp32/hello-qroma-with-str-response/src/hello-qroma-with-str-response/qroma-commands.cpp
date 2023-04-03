#include "qroma-commands.h"

extern QromaSerialCommApp myQromaApp;

void onHelloQroma(HelloQroma * message) {
  qromaAppSerialPrint("Hello ", &myQromaApp);
  qromaAppSerialPrintln(message->name, &myQromaApp);
}
