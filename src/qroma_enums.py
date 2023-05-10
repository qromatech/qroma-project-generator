from enum import Enum


class QromaProjectLocation(Enum):
    current_dir = "current_dir"
    qroma_project_dir = "qroma_project_dir"


class FirmwareFramework(str, Enum):
    platformio = "platformio"
    user_handled = "user_handled"
    # arduino = "arduino"
    # micropython = "micropython"


class ProtobufCompiler(str, Enum):
    nanopb = "nanopb"
    python = "python"
    typescript = "typescript"
    dart = "dart"


class ExitReason(Enum):
    UNSPECIFIED              = 1
    QROMA_DEV_INCOMPLETE     = 900
    INVALID_ENV              = 1000
    INVALID_ENV_NO_DOCKER    = 1001
    INVALID_PROJECT_FILE     = 1002
    INVALID_PROJECT_DIR      = 1003
    INVALID_USER_PROFILE     = 1004
    INVALID_USER_FW_PLATFORM = 1005

    UNABLE_TO_EDIT_PROTOBUFS = 1100
    UNABLE_TO_EDIT_FIRMWARE  = 1101
    UNABLE_TO_EDIT_APP       = 1102
    UNABLE_TO_EDIT_SITE      = 1103
