import os
import shutil

import qroma_dirs
import env_checks
from docker import docker_container_run, docker_container_rm
from qroma_enums import ExitReason
from qroma_project.qroma_project import QromaProject
from steps.pb import pb_install, pb_utils
from utils import typer_progress_message, qroma_exit_with_work, typer_show_lines_to_user


def run_pb_clean_step(qroma_project: QromaProject):
    with typer_progress_message("RUNNING PB CLEAN"):
        dirs_to_remove = pb_utils.get_dest_dirs_for_project(qroma_project)
        for dir_to_remove in dirs_to_remove:
            full_path_to_dir_to_remove = os.path.join(qroma_project.project_dir, dir_to_remove)
            if os.path.exists(full_path_to_dir_to_remove):
                with typer_progress_message(f"CLEAN PROTOBUF DIR: {full_path_to_dir_to_remove}"):
                    shutil.rmtree(full_path_to_dir_to_remove)


def run_pb_compile_step(qroma_project: QromaProject):
    docker_summary = env_checks.check_for_docker()
    if docker_summary is not None:
        with qroma_exit_with_work("UNABLE TO FIND DOCKER TO COMPILE PROTOCOL BUFFERS",
                                  ExitReason.INVALID_ENV_NO_DOCKER):
            env_checks.print_missing_tool_summary(docker_summary)

    src_and_dest_dirs = qroma_dirs.get_protobufs_build_src_and_dest_dirs(qroma_project)
    for (src_dir, dest_dir) in src_and_dest_dirs:
        with typer_progress_message(f"COMPILE PROTOBUF SUBPROCESS [{src_dir} -> {dest_dir}]"):

            docker_source_dir = "/usr/src/app/protofiles"
            docker_dest_dir = "/usr/src/app/outfiles"

            if os.path.exists(dest_dir):
                shutil.rmtree(dest_dir)

            docker_image_name = "devalbo/qroma-protobuf-compiler:v2"
            docker_container_name = "qroma-protobuf-compiler-1"

            with typer_progress_message(f"RUNNING DOCKER COMMAND TO COMPILE PROTOBUF"):
                output = docker_container_run(docker_image_name,
                                              docker_container_name,
                                              ["-v", f"{src_dir}:{docker_source_dir}",
                                               "-v", f"{dest_dir}:{docker_dest_dir}",
                                               ],
                                              )
                typer_show_lines_to_user(output)

            with typer_progress_message("CLEANING UP DOCKER IMAGE"):
                output = docker_container_rm(docker_container_name)
                typer_show_lines_to_user(output)


def run_pb_install_step(qroma_project: QromaProject):
    compilers_and_dest_dirs = pb_utils.get_compilers_and_dest_dirs_for_project(qroma_project)
    for (compiler, dest_dirs) in compilers_and_dest_dirs:
        pb_install.copy_compiled_dirs(qroma_project, compiler, dest_dirs)


def run_pb_build_step(qroma_project: QromaProject):
    run_pb_clean_step(qroma_project)
    run_pb_compile_step(qroma_project)
    run_pb_install_step(qroma_project)
