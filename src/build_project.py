from pydantic.dataclasses import dataclass
import subprocess

import qroma_dirs
from steps import pb_steps
from qroma_project.qroma_project import QromaProject
from utils import typer_progress_message


@dataclass
class BuildParameters:
    build_pb: bool = False
    build_firmware: bool = False
    build_site: bool = False

    def __init__(self, *,
                 build_pb=False,
                 build_firmware=False,
                 build_site=False,
                 ):
        self.build_pb = build_pb
        self.build_firmware = build_firmware
        self.build_site = build_site


def create_build_parameters_with_all_steps_disabled():
    return BuildParameters()


def create_build_parameters_with_all_steps_enabled():
    return BuildParameters(
        build_pb=True,
        build_firmware=True,
        build_site=True,
    )


def build_esp32_project_with_platformio(qroma_project: QromaProject):
    esp_project_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("RUNNING BUILD ESP 32 PROJECT SUBPROCESS IN " + esp_project_dir)
    subprocess.run(["pio", "run"], shell=True, cwd=esp_project_dir)
    print("DONE RUNNING BUILD PROJECT SUBPROCESS")


def build_site_www_project(qroma_project: QromaProject):
    site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    print("RUNNING BUILD WWW SITE SUBPROCESS")
    subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
    subprocess.run(["npm", "run", "build"], shell=True, cwd=site_www_dir)
    print("DONE RUNNING BUILD WWW SITE SUBPROCESS")


def run_build_projects(qroma_project: QromaProject, build_parameters: BuildParameters):
    with typer_progress_message("BUILD ALL PROJECTS"):
        if build_parameters.build_pb:
            pb_steps.run_pb_build_step(qroma_project)

        if build_parameters.build_firmware:
            build_esp32_project_with_platformio(qroma_project)

        if build_parameters.build_site:
            build_site_www_project(qroma_project)
        # print("DONE RUNNING BUILD ALL PROJECTS")


def do_build_project(qroma_project: QromaProject,
                     build_parameters: BuildParameters = create_build_parameters_with_all_steps_enabled(),
                     ):
    run_build_projects(qroma_project, build_parameters)
