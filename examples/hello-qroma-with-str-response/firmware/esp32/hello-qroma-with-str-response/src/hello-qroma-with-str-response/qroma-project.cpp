#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


int counter = 0;

void helloQromaWithStrResponseSetup()
{
  initQromaAppConfigWithDefaults(&_myQromaAppConfig, &qcMemBuffer, configQromaApp);
  startupQroma(&_myQromaAppConfig);

  delay(100);
}


void helloQromaWithStrResponseLoop()
{
  delay(1000);
}
