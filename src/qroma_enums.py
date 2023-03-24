from enum import Enum


class QromaProjectLocation(Enum):
    current_dir = "current_dir"
    qroma_project_dir = "qroma_project_dir"


class FirmwareFramework(str, Enum):
    platformio = "platformio"
    arduino = "arduino"
    # micropython = "micropython"


class ProtobufCompiler(str, Enum):
    nanopb = "nanopb"
    python = "python"
    typescript = "typescript"
    dart = "dart"


class ExitReason(Enum):
    UNSPECIFIED             = 1
    INVALID_ENV             = 1000
    INVALID_ENV_NO_DOCKER   = 1001
    INVALID_PROJECT_FILE    = 1002
    INVALID_USER_PROFILE    = 1003
