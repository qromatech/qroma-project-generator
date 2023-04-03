#include "qroma-commands.h"
#include "qroma-project.h"


void onMathProblem(MathProblem * message, MathProblemResponse * response) {
  switch (message->op)
  {
  case MathOperation_MathOp_Add:
    response->which_response = MathProblemResponse_addResult_tag;
    response->response.addResult.result = message->a + message->b;
    break;
  case MathOperation_MathOp_Subtract:
    response->which_response = MathProblemResponse_subtractResult_tag;
    response->response.subtractResult.result = message->a - message->b;
    break;
  case MathOperation_MathOp_Add_And_Subtract:
    response->which_response = MathProblemResponse_addAndSubtractResult_tag;
    response->response.addAndSubtractResult.addResult = message->a + message->b;
    response->response.addAndSubtractResult.subtractResult = message->a - message->b;
    break;
  default:
    break;
  }
}
