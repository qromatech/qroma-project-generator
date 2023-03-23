/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.5 */

#ifndef PB_QROMA_MONITOR_PB_H_INCLUDED
#define PB_QROMA_MONITOR_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Struct definitions */
typedef struct _QromaHeartbeat { 
    char heartbeatMessage[100]; 
    uint32_t uptime; 
} QromaHeartbeat;


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define QromaHeartbeat_init_default              {"", 0}
#define QromaHeartbeat_init_zero                 {"", 0}

/* Field tags (for use in manual encoding/decoding) */
#define QromaHeartbeat_heartbeatMessage_tag      1
#define QromaHeartbeat_uptime_tag                2

/* Struct field encoding specification for nanopb */
#define QromaHeartbeat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, STRING,   heartbeatMessage,   1) \
X(a, STATIC,   SINGULAR, UINT32,   uptime,            2)
#define QromaHeartbeat_CALLBACK NULL
#define QromaHeartbeat_DEFAULT NULL

extern const pb_msgdesc_t QromaHeartbeat_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define QromaHeartbeat_fields &QromaHeartbeat_msg

/* Maximum encoded size of messages (where known) */
#define QromaHeartbeat_size                      107

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
