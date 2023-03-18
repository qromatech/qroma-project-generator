import os.path

from qp_config import QromaProjectConfig
from qroma_project import QromaProject


def create_toml_str_list_str(key_name: str, l: list) -> str:
    if len(l) == 0:
        return f"{key_name} = []"
    if len(l) == 1:
        return f'{key_name} = ["{l[0]}"]'

    formatted_items = [f'  "{i}",\n' for i in l]
    content = "".join(formatted_items)
    return f"""{key_name} = [
  {content}
]"""


def create_toml_for_qroma_project_config(project_id: str, qpc: QromaProjectConfig) -> str:
    build_frameworks = create_toml_str_list_str("build_frameworks", [p.value for p in qpc.dev_board_platforms])
    return f"""
[qroma.project]
name = "{project_id}"
version = "0.1.0"


[qroma.project.dev_board]
{build_frameworks}


[qroma.project.run.commands.dev_boards.platformio]
build = "run"
install = "run --target upload --environment esp32dev"
monitor = ""
    """


def save_qroma_project(qp: QromaProject):
    s = create_toml_for_qroma_project_config(qp.project_id, qp.config)
    save_location = os.path.join(qp.project_dir, "qroma-draft.toml")
    with open(save_location, "w") as f:
        f.write(s)
