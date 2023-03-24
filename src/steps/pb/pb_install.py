import os.path
import shutil

import qroma_dirs
from qroma_enums import ProtobufCompiler
from qroma_project.qroma_project import QromaProject
from utils import typer_progress_message


def copy_compiled_dirs(qroma_project: QromaProject, language: ProtobufCompiler, language_dest_dirs: list[str]):
    src_and_dest_dirs = qroma_dirs.get_protobufs_build_src_and_dest_dirs(qroma_project)

    for (_, dest_dir) in src_and_dest_dirs:
        language_src_dir = os.path.join(dest_dir, language)
        full_language_dest_dirs = [os.path.join(qroma_project.project_dir, d) for d in language_dest_dirs]
        for language_dest_dir in full_language_dest_dirs:
            with typer_progress_message(f"REPLICATING [{language_src_dir} -> {language_dest_dir}]"):
                if os.path.exists(language_src_dir) and os.path.isdir(language_src_dir):
                    shutil.copytree(language_src_dir, language_dest_dir)
