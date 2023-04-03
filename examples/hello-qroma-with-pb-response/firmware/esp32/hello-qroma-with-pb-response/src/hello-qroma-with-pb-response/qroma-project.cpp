#include "qroma-project.h"
#include "qroma/qroma.h"
#include "qroma-commands.h"
#include "qroma/startup/configure/configureQromaApp.h"
#include "qroma/startup/configure/configureQromaSerialCommApp.h"

QromaSerialCommApp myQromaApp;


void helloQromaWithPbResponseSetup()
{
  registerPbCommandFunction<
    HelloQroma, HelloQroma_fields,
    HelloQromaResponse, HelloQromaResponse_fields
  >(onHelloQroma, &myQromaApp);

  configureQromaApp([](QromaAppConfig * config) {
    // config->loggerConfig.logLevel = Qroma_LogLevel_LogLevel_Info;
    config->loggerConfig.logLevel = Qroma_LogLevel_LogLevel_Error;
  }, &myQromaApp);

  configureSerialCommIo([](QromaCommSerialIoConfig * config) {
    config->baudRate = 115200;
    config->rxBufferSize = 1000;
    config->txBufferSize = 1000;
  }, &myQromaApp);

  startupQroma(&myQromaApp);

  delay(100);
}


void helloQromaWithPbResponseLoop()
{
  delay(1000);
}
