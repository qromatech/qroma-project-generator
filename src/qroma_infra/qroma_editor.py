import os

import typer

from qroma_enums import ExitReason
from qroma_project.qroma_project import QromaProject
from utils import qroma_edit_dir, prompt_user_for_dir_choice


def open_pb_editor(qroma_project: QromaProject):
    candidates_dir_path = os.path.join(qroma_project.project_dir, "protobufs")
    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_PROTOBUFS.value)


def open_firmware_editor(qroma_project: QromaProject):
    candidates_dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)
    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_FIRMWARE.value)


def open_app_editor(qroma_project: QromaProject):
    candidates_dir_path = os.path.join(qroma_project.project_dir, "apps")
    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_APP.value)


def open_site_editor(qroma_project: QromaProject):
    candidates_dir_path = os.path.join(qroma_project.project_dir, "sites",)
    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_SITE.value)
