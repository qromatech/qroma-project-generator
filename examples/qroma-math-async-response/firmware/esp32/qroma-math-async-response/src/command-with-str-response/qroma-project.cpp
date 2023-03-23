#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


int counter = 0;

void qromaProjectSetup()
{
  initQromaAppConfigWithDefaults(&_myQromaAppConfig, &qcMemBuffer, configQromaApp);
  startupQroma(&_myQromaAppConfig);

  delay(100);
}


void qromaProjectLoop()
{
  QromaHeartbeat qhb = QromaHeartbeat();

  char tickBuffer[10];
  itoa(counter, tickBuffer, 10);
  counter++;

  strncat(qhb.heartbeatMessage, "Qroma tick: ", sizeof(QromaHeartbeat::heartbeatMessage) - 1);
  strncat(qhb.heartbeatMessage, tickBuffer, sizeof(QromaHeartbeat::heartbeatMessage) - 1);
  qhb.uptime = millis();

  sendSerialPbMessage<QromaHeartbeat, QromaHeartbeat_fields>(&qhb);

  delay(1000);
}
