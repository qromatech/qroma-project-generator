#include "qroma-commands.h"
#include "qroma/qroma-comm/qroma-comm.h"
#include "qroma/qroma.h"

extern QromaSerialCommApp myQromaApp;

void onHelloQroma(HelloQroma * message) {
  qromaAppSerialPrint("Hello str: ", &myQromaApp);
  qromaAppSerialPrintln(message->name, &myQromaApp);
}
