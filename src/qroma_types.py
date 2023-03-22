# from dataclasses import dataclass
# from typing import List
import os
from enum import Enum
from pydantic.dataclasses import dataclass

# from qroma_enums import DeviceBoardPlatform
from build_project import BuildParameters
from qp_config import QromaProjectConfig
# from qp_new.project_template import NewQromaProjectException, is_valid_project_id, QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX
from qroma_enums import QromaProjectLocation


@dataclass
class NewQromaProjectInfoFromUserInput:
    project_id: str
    project_dir: str
    project_location: QromaProjectLocation
    project_dir_exists: bool

#
# @dataclass
# class ExistingQromaProjectInfoFromUserInput:
#     project_id: str
#     project_dir: str
#     project_location: QromaProjectLocation

#
# import click
#
# from qroma_project import QROMA_PROJECTS_ROOT_DIR
#
#
# @dataclass
# class _QromaProjectInfoFromUserInput:
#     project_id: str
#     project_dir: str
#     project_location: QromaProjectLocation
#
#
# def get_qroma_project_info_from_user_input(user_project_id: str | None) -> _QromaProjectInfoFromUserInput:
#     project_id = user_project_id
#     if not is_valid_project_id(project_id):
#         raise NewQromaProjectException(f"Invalid project ID: {project_id}")
#
#     project_dir = os.getcwd()
#     project_location = QromaProjectLocation.current_dir
#
#     if user_project_id.startswith(QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX):
#         project_id = user_project_id[1:]
#         project_dir = os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#         project_location = QromaProjectLocation.qroma_project_dir
#
#     project_exists = os.path.exists(project_dir)
#     if not project_exists:
#         project_location = QromaProjectLocation.does_not_exist
#
#     return _QromaProjectInfoFromUserInput(
#         project_dir,
#         project_id,
#         project_location,
#     )

#
# class QromaProjectInfoFromUserInput(click.ParamType):
#
#     def convert(self, value, param, ctx):
#         return _QromaProjectInfoFromUserInput(value)
#         # project_id: str
#         # project_dir: str
#         # project_location: QromaProjectLocation


@dataclass
class GenerateProjectOptions:
    project_config: QromaProjectConfig
    build_parameters: BuildParameters
    replace_existing_project_directory: bool
