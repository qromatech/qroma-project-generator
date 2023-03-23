/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.5 */

#ifndef PB_HELLO_QROMA_PB_H_INCLUDED
#define PB_HELLO_QROMA_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
typedef enum _MathOperation { 
    MathOperation_MathOp_NotSet = 0, 
    MathOperation_MathOp_Add = 1, 
    MathOperation_MathOp_Subtract = 2, 
    MathOperation_MathOp_Add_And_Subtract = 3 
} MathOperation;

/* Struct definitions */
typedef struct _HelloQroma { 
    char name[20]; 
} HelloQroma;

typedef struct _HelloQromaResponse { 
    char response[30]; 
    uint32_t callCount; 
    uint32_t nameLength; 
} HelloQromaResponse;

typedef struct _MathProblem { 
    uint32_t a; 
    uint32_t b; 
    MathOperation op; 
} MathProblem;

typedef struct _MathResult_Add { 
    uint32_t result; 
} MathResult_Add;

typedef struct _MathResult_AddAndSubtract { 
    uint32_t addResult; 
    uint32_t subtractResult; 
} MathResult_AddAndSubtract;

typedef struct _MathResult_Subtract { 
    uint32_t result; 
} MathResult_Subtract;

typedef struct _QromaHeartbeat { 
    char heartbeatMessage[100]; 
    uint32_t uptime; 
} QromaHeartbeat;

typedef struct _MathResponse { 
    pb_size_t which_response;
    union {
        MathResult_Add addResult;
        MathResult_Subtract subtractResult;
        MathResult_AddAndSubtract addAndSubtractResult;
    } response; 
} MathResponse;


/* Helper constants for enums */
#define _MathOperation_MIN MathOperation_MathOp_NotSet
#define _MathOperation_MAX MathOperation_MathOp_Add_And_Subtract
#define _MathOperation_ARRAYSIZE ((MathOperation)(MathOperation_MathOp_Add_And_Subtract+1))


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define QromaHeartbeat_init_default              {"", 0}
#define HelloQroma_init_default                  {""}
#define HelloQromaResponse_init_default          {"", 0, 0}
#define MathProblem_init_default                 {0, 0, _MathOperation_MIN}
#define MathResult_Add_init_default              {0}
#define MathResult_Subtract_init_default         {0}
#define MathResult_AddAndSubtract_init_default   {0, 0}
#define MathResponse_init_default                {0, {MathResult_Add_init_default}}
#define QromaHeartbeat_init_zero                 {"", 0}
#define HelloQroma_init_zero                     {""}
#define HelloQromaResponse_init_zero             {"", 0, 0}
#define MathProblem_init_zero                    {0, 0, _MathOperation_MIN}
#define MathResult_Add_init_zero                 {0}
#define MathResult_Subtract_init_zero            {0}
#define MathResult_AddAndSubtract_init_zero      {0, 0}
#define MathResponse_init_zero                   {0, {MathResult_Add_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define HelloQroma_name_tag                      1
#define HelloQromaResponse_response_tag          1
#define HelloQromaResponse_callCount_tag         2
#define HelloQromaResponse_nameLength_tag        3
#define MathProblem_a_tag                        1
#define MathProblem_b_tag                        2
#define MathProblem_op_tag                       3
#define MathResult_Add_result_tag                1
#define MathResult_AddAndSubtract_addResult_tag  1
#define MathResult_AddAndSubtract_subtractResult_tag 2
#define MathResult_Subtract_result_tag           1
#define QromaHeartbeat_heartbeatMessage_tag      1
#define QromaHeartbeat_uptime_tag                2
#define MathResponse_addResult_tag               1
#define MathResponse_subtractResult_tag          2
#define MathResponse_addAndSubtractResult_tag    3

/* Struct field encoding specification for nanopb */
#define QromaHeartbeat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, STRING,   heartbeatMessage,   1) \
X(a, STATIC,   SINGULAR, UINT32,   uptime,            2)
#define QromaHeartbeat_CALLBACK NULL
#define QromaHeartbeat_DEFAULT NULL

#define HelloQroma_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, STRING,   name,              1)
#define HelloQroma_CALLBACK NULL
#define HelloQroma_DEFAULT NULL

#define HelloQromaResponse_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, STRING,   response,          1) \
X(a, STATIC,   SINGULAR, UINT32,   callCount,         2) \
X(a, STATIC,   SINGULAR, UINT32,   nameLength,        3)
#define HelloQromaResponse_CALLBACK NULL
#define HelloQromaResponse_DEFAULT NULL

#define MathProblem_FIELDLIST(X, a_) \
X(a_, STATIC,   SINGULAR, UINT32,   a,                 1) \
X(a_, STATIC,   SINGULAR, UINT32,   b,                 2) \
X(a_, STATIC,   SINGULAR, UENUM,    op,                3)
#define MathProblem_CALLBACK NULL
#define MathProblem_DEFAULT NULL

#define MathResult_Add_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   result,            1)
#define MathResult_Add_CALLBACK NULL
#define MathResult_Add_DEFAULT NULL

#define MathResult_Subtract_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   result,            1)
#define MathResult_Subtract_CALLBACK NULL
#define MathResult_Subtract_DEFAULT NULL

#define MathResult_AddAndSubtract_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   addResult,         1) \
X(a, STATIC,   SINGULAR, UINT32,   subtractResult,    2)
#define MathResult_AddAndSubtract_CALLBACK NULL
#define MathResult_AddAndSubtract_DEFAULT NULL

#define MathResponse_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (response,addResult,response.addResult),   1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (response,subtractResult,response.subtractResult),   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (response,addAndSubtractResult,response.addAndSubtractResult),   3)
#define MathResponse_CALLBACK NULL
#define MathResponse_DEFAULT NULL
#define MathResponse_response_addResult_MSGTYPE MathResult_Add
#define MathResponse_response_subtractResult_MSGTYPE MathResult_Subtract
#define MathResponse_response_addAndSubtractResult_MSGTYPE MathResult_AddAndSubtract

extern const pb_msgdesc_t QromaHeartbeat_msg;
extern const pb_msgdesc_t HelloQroma_msg;
extern const pb_msgdesc_t HelloQromaResponse_msg;
extern const pb_msgdesc_t MathProblem_msg;
extern const pb_msgdesc_t MathResult_Add_msg;
extern const pb_msgdesc_t MathResult_Subtract_msg;
extern const pb_msgdesc_t MathResult_AddAndSubtract_msg;
extern const pb_msgdesc_t MathResponse_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define QromaHeartbeat_fields &QromaHeartbeat_msg
#define HelloQroma_fields &HelloQroma_msg
#define HelloQromaResponse_fields &HelloQromaResponse_msg
#define MathProblem_fields &MathProblem_msg
#define MathResult_Add_fields &MathResult_Add_msg
#define MathResult_Subtract_fields &MathResult_Subtract_msg
#define MathResult_AddAndSubtract_fields &MathResult_AddAndSubtract_msg
#define MathResponse_fields &MathResponse_msg

/* Maximum encoded size of messages (where known) */
#define HelloQromaResponse_size                  43
#define HelloQroma_size                          21
#define MathProblem_size                         14
#define MathResponse_size                        14
#define MathResult_AddAndSubtract_size           12
#define MathResult_Add_size                      6
#define MathResult_Subtract_size                 6
#define QromaHeartbeat_size                      107

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif