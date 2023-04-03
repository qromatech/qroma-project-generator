#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


void helloQromaWithPbResponseSetup()
{
  startupQroma(&qcMemBuffer, configQromaApp);

  delay(100);
}


void helloQromaWithPbResponseLoop()
{
  delay(1000);
}
