#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


int counter = 0;

void helloQromaWithPbResponseSetup()
{
  initQromaAppConfigWithDefaults(&_myQromaAppConfig, &qcMemBuffer, configQromaApp);
  startupQroma(&_myQromaAppConfig);

  delay(100);
}


void helloQromaWithPbResponseLoop()
{
  delay(1000);
}
