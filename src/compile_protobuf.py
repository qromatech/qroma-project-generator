import os
import shutil
import subprocess
from typing import Optional

import qroma_dirs
from qroma_project import load_current_dir_qroma_project, QromaProject, load_qroma_project_from_directory


def run_pb_compile(qroma_project: QromaProject):
    protobufs_dir = qroma_dirs.get_protobufs_dir(qroma_project)
    print(f"RUNNING COMPILER IN {protobufs_dir}")
    subprocess.run(["docker-protobuf-compile.bat"],
                   shell=True,
                   cwd=protobufs_dir)
    print("DONE RUNNING COMPILE PROTOBUF SUBPROCESS")


def clean_esp32_protobuf_dirs(qroma_project: QromaProject):
    esp_project_pb_dir = qroma_dirs.get_esp_project_pb_dir(qroma_project)
    print(f"CHECKING FOR ESP PROJECT PROTOBUF DIR: {esp_project_pb_dir}")
    if os.path.exists(esp_project_pb_dir):
        print("CLEANING OUT ESP PROJECT PROTOBUF DIRS")
        shutil.rmtree(esp_project_pb_dir)
        print("DONE CLEANING OUT ESP PROJECT PROTOBUF DIRS")


def copy_nanopb_to_esp32_dir(qroma_project: QromaProject):
    copy_from_dir = qroma_dirs.get_protobufs_out_nanopb_dir(qroma_project)
    copy_to_dir = qroma_dirs.get_esp_project_pb_dir(qroma_project)
    print(f"COPYING NANOPB PROTOBUFS FROM {copy_from_dir} TO {copy_to_dir}")
    shutil.copytree(copy_from_dir, copy_to_dir)
    print("DONE COPYING NANOPB PROTOBUFS")


def do_compile_protobuf(project_id: Optional[str]):
    if project_id is None:
        qroma_project = load_current_dir_qroma_project()
    else:
        project_dir = os.path.join(os.getcwd(), project_id)
        qroma_project = load_qroma_project_from_directory(project_dir)

    run_pb_compile(qroma_project)
    clean_esp32_protobuf_dirs(qroma_project)
    copy_nanopb_to_esp32_dir(qroma_project)
