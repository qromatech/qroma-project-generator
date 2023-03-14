import sys, os
from pathlib import Path

import env_checks, device_boards, project_template
from qroma_project import QromaProject, save_qroma_project


def do_generate_project(project_id, project_root_dir) -> QromaProject:
    # make sure you have docker and npm installed
    env_checks.do_env_checks()

    # # ask user for project ID that can also be a directory name
    # project_id = project_template.get_project_id_from_user()

    # download and unzip template contents from https://github.com/qromatech/qroma-project-template
    project_dir = project_template.setup_project_directory(project_id, project_root_dir)

    # use project ID to name Arduino project directory
    device_boards.setup_device_project(project_dir, project_id)

    # setup web sites for interacting with project installed on board
    # www_sites.do_docusaurus_setup(project_dir, project_id)

    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        print("QROMA-CLI PATH")
        print(sys.executable)
        project_app_path = os.path.join(project_dir, "qroma.exe")
        print(project_app_path)
        # shutil.copy(application_path, project_app_path)

    else:
        print("RUNNING FROM PYTHON EXECUTABLE, NOT AS CLI APP")

    this_project: QromaProject = QromaProject(project_dir, project_id)
    save_location = Path(os.path.join(project_dir, "qroma.yaml"))
    save_qroma_project(this_project, save_location)

    return this_project
