from enum import Enum


class QromaProjectLocation(Enum):
    current_dir = "current_dir"
    qroma_project_dir = "qroma_project_dir"


class FirmwareFramework(str, Enum):
    user_managed = "user_managed"
    platformio = "platformio"
    # arduino = "arduino"
    # arduino_cli = "arduino_cli
    # micropython = "micropython"


class ProtobufCompiler(str, Enum):
    nanopb = "nanopb"
    python = "python"
    typescript = "typescript"
    dart = "dart"


class ExitReason(Enum):
    UNSPECIFIED                     = 1
    QROMA_DEV_INCOMPLETE            = 900
    INVALID_ENV                     = 1000
    INVALID_PROJECT_FILE            = 1002
    INVALID_PROJECT_DIR             = 1003
    INVALID_USER_PROFILE            = 1004
    INVALID_USER_FW_PLATFORM        = 1005
    INVALID_ENV_ALREADY_GIT_REPO    = 1006
    INVALID_ENV_NOT_A_GIT_REPO      = 1007

    UNABLE_TO_EDIT_PROTOBUFS        = 1100
    UNABLE_TO_EDIT_FIRMWARE         = 1101
    UNABLE_TO_EDIT_APP              = 1102
    UNABLE_TO_EDIT_SITE             = 1103

    MISSING_TOOL_DOCKER             = 1201
    MISSING_TOOL_GIT                = 1202

    BUNDLE_FIRMWARE_MISSING_FILE    = 1300
    TEMPLATE_FILES_MISMATCH         = 1301
