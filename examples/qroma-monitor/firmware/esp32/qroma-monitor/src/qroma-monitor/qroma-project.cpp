#include "qroma-project.h"
#include "qroma/qroma.h"
#include "../qroma-proto/qroma-monitor.pb.h"


#define COMM_BUFFER_SIZE 100
uint8_t _commBuffer[COMM_BUFFER_SIZE];
QromaCommMemBuffer qcMemBuffer = QromaCommMemBuffer(_commBuffer, COMM_BUFFER_SIZE);


int counter = 0;

void qromaMonitorSetup()
{
  startupQroma(&qcMemBuffer);

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

  sendSerialPbMessage<QromaHeartbeat, QromaHeartbeat_fields>(&qhb);

  delay(1000);
}
