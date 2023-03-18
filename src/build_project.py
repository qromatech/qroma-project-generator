# from dataclasses import dataclass
from pydantic.dataclasses import dataclass
import subprocess

import qroma_dirs
from qroma_project import QromaProject
import compile_protobuf


@dataclass
class BuildParameters:
    include_pb: bool = False
    include_device: bool = False
    include_site: bool = False

    def __init__(self, *,
                 include_pb=False,
                 include_device=False,
                 include_site=False,
                 ):
        self.include_pb = include_pb
        self.include_device = include_device
        self.include_site = include_site


def create_build_parameters_with_all_steps_disabled():
    return BuildParameters()


def create_build_parameters_with_all_steps_enabled():
    return BuildParameters(
        include_pb=True,
        include_device=True,
        include_site=True,
    )


def build_esp32_project_with_platformio(qroma_project: QromaProject):
    esp_project_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("RUNNING BUILD ESP 32 PROJECT SUBPROCESS")
    subprocess.run(["pio", "run"], shell=True, cwd=esp_project_dir)
    print("DONE RUNNING BUILD PROJECT SUBPROCESS")


def build_site_www_project(qroma_project: QromaProject):
    site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    print("RUNNING BUILD WWW SITE SUBPROCESS")
    subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
    subprocess.run(["npm", "run", "build"], shell=True, cwd=site_www_dir)
    print("DONE RUNNING BUILD WWW SITE SUBPROCESS")


def run_build_projects(qroma_project: QromaProject, build_parameters: BuildParameters):
    print("RUNNING BUILD ALL PROJECTS")
    if build_parameters.include_pb:
        compile_protobuf.do_compile_protobuf(qroma_project)

    if build_parameters.include_device:
        build_esp32_project_with_platformio(qroma_project)

    if build_parameters.include_site:
        build_site_www_project(qroma_project)
    print("DONE RUNNING BUILD ALL PROJECTS")


def do_build_project(qroma_project: QromaProject,
                     build_parameters: BuildParameters = create_build_parameters_with_all_steps_enabled(),
                     ):
    run_build_projects(qroma_project, build_parameters)
