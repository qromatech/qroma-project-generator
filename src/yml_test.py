import os
from pathlib import Path

import qroma_project
from qroma_project import QromaProject
# from qroma_project import QromaCliInfo, save_cli_info, load_cli_info

project_id = "d"


cli_info: QromaProject = QromaProject(project_id)
qroma_project.save_qroma_project(cli_info, project_id)


loaded = qroma_project.load_qroma_project(project_id)
print("LOADED")
print(loaded)
