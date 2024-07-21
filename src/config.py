
LOCAL_TEMPLATE_DIR = "./qroma-project-template"
LOCAL_PROJECT_TEMPLATE_RESOURCES_DIR = "./project_template_resources"

QROMA_PROJECT_TEMPLATE_BRANCH_NAME = "main"
# QROMA_PROJECT_TEMPLATE_BRANCH_NAME = "qroma-core"
QROMA_PROJECT_TEMPLATE_ZIP_URL = f'https://github.com/qromatech/qroma-project-template/archive/refs/heads/{QROMA_PROJECT_TEMPLATE_BRANCH_NAME}.zip'
LOCAL_TEMPLATE_QROMA_PROJECT_ZIP_FILENAME = f"qroma-project-template-{QROMA_PROJECT_TEMPLATE_BRANCH_NAME}.zip"

REACT_QROMA_LIB_BRANCH_NAME = "main"
# REACT_QROMA_LIB_BRANCH_NAME = "qroma-core"
REACT_QROMA_LIB_ZIP_URL = f"https://github.com/qromatech/react-qroma-lib/archive/refs/heads/{REACT_QROMA_LIB_BRANCH_NAME}.zip"
LOCAL_TEMPLATE_REACT_QROMA_LIB_ZIP_FILENAME = f"react-qroma-lib-{REACT_QROMA_LIB_BRANCH_NAME}.zip"


TEMPLATE_SOURCE_ZIP_URLS_AND_LOCAL_FILENAMES = (
    (LOCAL_TEMPLATE_QROMA_PROJECT_ZIP_FILENAME, QROMA_PROJECT_TEMPLATE_ZIP_URL),
    (LOCAL_TEMPLATE_REACT_QROMA_LIB_ZIP_FILENAME, REACT_QROMA_LIB_ZIP_URL),
)

JINJA_TEST_TEMPLATE_DIR = "../jinja_dir_test/QROMA-PROJECT-TEMPLATE"


DOCKER_PB_COMPILE_SOURCE_DIR = "/usr/src/app/protofiles"
DOCKER_PB_COMPILE_DEST_DIR = "/usr/src/app/outfiles"
# DOCKER_PB_COMPILE_IMAGE_NAME = "devalbo/qroma-protobuf-compiler:v2"
# DOCKER_PB_COMPILE_CONTAINER_NAME = "qroma-protobuf-compiler-1"
DOCKER_PB_COMPILE_IMAGE_NAME = "devalbo/qroma-project-generator-tools:v2"
DOCKER_PB_COMPILE_CONTAINER_NAME = "qroma-project-generator-tools-2"

