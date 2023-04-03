#ifndef QROMA_COMMANDS_H
#define QROMA_COMMANDS_H

#include "qroma/qroma.h"
#include "../qroma-proto/qroma-math-async-response.pb.h"

void onMathProblem(MathProblem * message, MathProblemResponse * response);

#endif
