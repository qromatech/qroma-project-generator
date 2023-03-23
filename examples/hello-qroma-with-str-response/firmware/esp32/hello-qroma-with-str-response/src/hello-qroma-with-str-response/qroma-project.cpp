#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


void helloQromaWithStrResponseSetup()
{
  startupQroma(&qcMemBuffer, configQromaApp);
  delay(100);
}


void helloQromaWithStrResponseLoop()
{
  delay(1000);
}
