#include "qroma-project.h"
#include "qroma-config.h"
#include "qroma/qroma.h"


// #define COMM_BUFFER_SIZE 100
// uint8_t _commBuffer[COMM_BUFFER_SIZE];
// QromaCommMemBuffer qcMemBuffer = QromaCommMemBuffer(_commBuffer, COMM_BUFFER_SIZE);


void helloQromaWithPbResponseSetup()
{
  startupQroma(&qcMemBuffer, configQromaApp);

  delay(100);
}


void helloQromaWithPbResponseLoop()
{
  // Serial.println("TI-CK");
  delay(1000);
}
