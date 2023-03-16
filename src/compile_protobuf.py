import os
import shutil
import subprocess
from typing import Optional

import qroma_dirs
import env_checks
import constants
from qroma_project import load_current_dir_qroma_project, QromaProject, load_qroma_project_from_directory


def run_pb_compile(qroma_project: QromaProject):
    docker_summary = env_checks.check_for_docker()
    if docker_summary is not None:
        print("UNABLE TO FIND DOCKER TO COMPILE PROTOCOL BUFFERS")
        env_checks.print_missing_tool_summary(docker_summary)
        exit(constants.EXIT_CODE_INVALID_ENV_NO_DOCKER)

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
        print("CLEANING OUT ESP PROJECT PROTOBUF DIR")
        shutil.rmtree(esp_project_pb_dir)
        print("DONE CLEANING OUT ESP PROJECT PROTOBUF DIR")


def copy_nanopb_to_esp32_dir(qroma_project: QromaProject):
    copy_from_dir = qroma_dirs.get_protobufs_out_nanopb_dir(qroma_project)
    copy_to_dir = qroma_dirs.get_esp_project_pb_dir(qroma_project)
    print(f"COPYING NANOPB PROTOBUFS FROM {copy_from_dir} TO {copy_to_dir}")
    shutil.copytree(copy_from_dir, copy_to_dir)
    print("DONE COPYING NANOPB PROTOBUFS")


def clean_site_www_protobuf_dirs(qroma_project: QromaProject):
    site_www_pb_dir = qroma_dirs.get_site_www_pb_dir(qroma_project)
    print(f"CHECKING FOR SITE WWW PROTOBUF DIR: {site_www_pb_dir}")
    if os.path.exists(site_www_pb_dir):
        print("CLEANING OUT SITE WWW PROTOBUF DIR")
        shutil.rmtree(site_www_pb_dir)
        print("DONE CLEANING OUT SITE WWW PROTOBUF DIR")


def copy_typescriptpb_to_site_www_dir(qroma_project: QromaProject):
    copy_from_dir = qroma_dirs.get_protobufs_out_typescriptpb_dir(qroma_project)
    copy_to_dir = qroma_dirs.get_site_www_pb_dir(qroma_project)
    print(f"COPYING SITE WWW PROTOBUFS FROM {copy_from_dir} TO {copy_to_dir}")
    shutil.copytree(copy_from_dir, copy_to_dir)
    print("DONE COPYING SITE WWW PROTOBUFS")


def do_compile_protobuf(qroma_project: QromaProject):
    # if project_id is None:
    #     qroma_project = load_current_dir_qroma_project()
    # else:
    #     project_dir = os.path.join(os.getcwd(), project_id)
    #     qroma_project = load_qroma_project_from_directory(project_dir)

    run_pb_compile(qroma_project)

    clean_esp32_protobuf_dirs(qroma_project)
    copy_nanopb_to_esp32_dir(qroma_project)

    clean_site_www_protobuf_dirs(qroma_project)
    copy_typescriptpb_to_site_www_dir(qroma_project)
