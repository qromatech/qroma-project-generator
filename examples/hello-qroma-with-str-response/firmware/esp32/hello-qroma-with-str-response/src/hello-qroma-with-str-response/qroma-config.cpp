#include "qroma-commands.h"

QromaBytesProcessor *qromaBytesProcessors[] = { &helloQromaPbProcessor, };


#define COMM_BUFFER_SIZE 100
uint8_t _commBuffer[COMM_BUFFER_SIZE];
QromaCommMemBuffer qcMemBuffer = QromaCommMemBuffer(_commBuffer, COMM_BUFFER_SIZE);


void configQromaApp(QromaAppConfig * config) {
  config->serialIoConfig.qromaBytesProcessors = qromaBytesProcessors;
  config->serialIoConfig.qromaBytesProcessorsCount = sizeof(qromaBytesProcessors) / sizeof(QromaBytesProcessor*);

  //  config->loggerConfig.logLevel = Qroma_LogLevel_LogLevel_Info;
   config->loggerConfig.logLevel = Qroma_LogLevel_LogLevel_Error;
}
