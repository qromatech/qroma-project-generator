from pydantic.dataclasses import dataclass

from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps import pb_steps, firmware_steps, site_steps
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


def run_build_projects(qroma_project: QromaProject, user_profile: QromaUserProfile, build_parameters: BuildParameters):
    with typer_progress_message("BUILD ALL PROJECTS"):
        print(build_parameters)
        if build_parameters.build_pb:
            pb_steps.run_pb_build_step(qroma_project)

        if build_parameters.build_firmware:
            firmware_steps.run_firmware_build_step(qroma_project, user_profile)

        if build_parameters.build_site:
            site_steps.run_site_bundle_step(qroma_project)
            site_steps.run_site_npm_install_step(qroma_project)

        print("DONE RUNNING BUILD ALL PROJECTS")


def do_build_project(qroma_project: QromaProject,
                     user_profile: QromaUserProfile,
                     build_parameters: BuildParameters = create_build_parameters_with_all_steps_enabled(),
                     ):
    run_build_projects(qroma_project, user_profile, build_parameters)
