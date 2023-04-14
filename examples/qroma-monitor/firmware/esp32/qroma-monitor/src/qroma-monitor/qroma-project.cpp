#include "qroma-project.h"
#include "qroma/qroma.h"
#include "../qroma-proto/qroma-monitor.pb.h"


int counter = 0;
QromaSerialCommApp myQromaApp;


void qromaMonitorSetup()
{
  startupQroma(&myQromaApp);

  delay(100);
}


void qromaMonitorLoop()
{
  QromaHeartbeat qhb = QromaHeartbeat();

  char tickBuffer[10];
  itoa(counter, tickBuffer, 10);
  counter++;

  strncat(qhb.heartbeatMessage, "Qroma tick: ", sizeof(QromaHeartbeat::heartbeatMessage) - 1);
  strncat(qhb.heartbeatMessage, tickBuffer, sizeof(QromaHeartbeat::heartbeatMessage) - 1);
  qhb.uptime = millis();

  sendSerialPb64NewLineMessage<QromaHeartbeat, QromaHeartbeat_fields>(&qhb, &myQromaApp);

  delay(1000);
}
