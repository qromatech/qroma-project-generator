from qp_config.qroma_project_config import MakeProtobufStage
from qroma_project.qroma_project import QromaProject


def get_protobuf_stage_config(qroma_project: QromaProject) -> MakeProtobufStage:
    pb_build_stage = qroma_project.config.qroma.project.stages.sw.protobuf
    return pb_build_stage
