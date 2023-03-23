#ifndef QROMA_CONFIG_H
#define QROMA_CONFIG_H

#include "qroma/qroma.h"
#include "../qroma-proto/hello-qroma-with-str-response.pb.h"


extern QromaCommMemBuffer qcMemBuffer;

void configQromaApp(QromaAppConfig * config);

#endif
