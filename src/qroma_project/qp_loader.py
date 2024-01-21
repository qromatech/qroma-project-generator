import os
import tomllib
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, BaseLoader

from qp_config.qroma_project_basics import create_project_basics, QromaProjectBasics
from qp_config.qroma_project_config import create_project_config
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_infra.qroma_project_file_template_values import create_qroma_project_file_template_values
from qroma_project.qroma_project import QromaProject, QROMA_PROJECT_CONFIG_FILE_NAME
from typing import Optional

from qroma_user_profile.qroma_user_profile import QromaUserProfile


def load_qroma_project(qroma_project: QromaProject) -> Optional[QromaProject]:
    return load_qroma_project_from_directory(qroma_project.project_dir)


def load_qroma_project_from_directory(qroma_dir: str | os.PathLike) -> Optional[QromaProject]:
    qroma_project_config_file_path = Path(qroma_dir, QROMA_PROJECT_CONFIG_FILE_NAME)
    return load_qroma_project_from_file(qroma_project_config_file_path)


def load_qroma_basics_from_file(qroma_project_config_file_location: str | os.PathLike) -> Optional[QromaProjectBasics]:
    try:
        with open(qroma_project_config_file_location, 'rb') as file:
            qroma_basics_dict = tomllib.load(file)
            qroma_project_basics = QromaProjectBasics(**qroma_basics_dict)
            return qroma_project_basics
        
    except FileNotFoundError:
        return None
    

def load_qroma_project_from_file(user_profile: QromaUserProfile, qroma_project_config_file_location: str | os.PathLike) -> Optional[QromaProject]:
    try:
        with open(qroma_project_config_file_location, 'r') as f:
            file_contents = f.read()

            project_root_dir = os.path.dirname(qroma_project_config_file_location)
            project_root_dir = project_root_dir.replace("\\", "/")

            template = Environment(loader=BaseLoader()).from_string(file_contents)

            qroma_basics_toml = template.render(qroma_project_dir=project_root_dir, qroma={
                "project_dirs": {},
                "user_profile_dirs": {},
            })

            qroma_basics_dict = tomllib.loads(qroma_basics_toml)
            qroma_project_basics = QromaProjectBasics(**qroma_basics_dict)

            qroma = create_qroma_project_file_template_values(project_root_dir, qroma_project_basics, user_profile)
            project_from_template = template.render(qroma_project_dir=project_root_dir, qroma=qroma)

            config_used_qroma_project_path = os.path.join(project_root_dir, "qroma-resolved.toml")
            with open(config_used_qroma_project_path, "w") as qrf:
                qrf.write(project_from_template)

            qroma_dict = tomllib.loads(project_from_template)

            qp = QromaProject(
                project_dir=os.path.dirname(qroma_project_config_file_location),
                project_id=qroma_dict['qroma']['project']['id']
            )

            qp_config = create_project_config(qroma_dict)
            qp.set_config(qp_config)

            return qp

    except FileNotFoundError:
        return None


def load_current_dir_qroma_project() -> QromaProject:
    user_profile = load_qroma_user_profile()
    dir_to_check = Path(os.getcwd()).absolute()

    while True:
        qroma_project_config_file_path = Path(os.path.join(dir_to_check, QROMA_PROJECT_CONFIG_FILE_NAME))
        qroma_project = load_qroma_project_from_file(user_profile, qroma_project_config_file_path)

        if qroma_project is not None:
            return qroma_project

        parent_dir = Path(os.path.dirname(dir_to_check)).absolute()
        if parent_dir.samefile(dir_to_check.anchor):
            # we are at the root
            print(f"NO qroma project found in {os.getcwd()} or its parent paths")
            return None

        dir_to_check = parent_dir
