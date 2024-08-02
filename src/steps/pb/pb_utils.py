from qp_config import qp_config_shortcuts
from qroma_enums import ProtobufCompiler
from qroma_project.qroma_project import QromaProject


def get_compilers_and_dest_dirs_for_project(qroma_project: QromaProject):
    pb_stage_config = qp_config_shortcuts.get_protobuf_stage_config(qroma_project)
    compilers_and_dest_dirs = [
        (ProtobufCompiler.nanopb, pb_stage_config.replication.nanopb.dirs),
        (ProtobufCompiler.python, pb_stage_config.replication.python.dirs),
        (ProtobufCompiler.typescript, pb_stage_config.replication.typescript.dirs),
        (ProtobufCompiler.dart, pb_stage_config.replication.dart.dirs),
        (ProtobufCompiler.rust, pb_stage_config.replication.rust.dirs),
    ]
    return compilers_and_dest_dirs


def get_dest_dirs_for_project(qroma_project: QromaProject) -> list[str]:
    compilers_and_dest_dirs = get_compilers_and_dest_dirs_for_project(qroma_project)
    dest_dirs_for_compilers = [d for (c, d) in compilers_and_dest_dirs]

    dest_dirs = []
    for compiler_dest_dirs in dest_dirs_for_compilers:
        dest_dirs.extend(compiler_dest_dirs)

    return dest_dirs
