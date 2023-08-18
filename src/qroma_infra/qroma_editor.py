from enum import Enum

import typer

from qroma_enums import ExitReason
from qroma_project.qroma_project import QromaProject
from utils import qroma_edit_dir, prompt_user_for_dir_choice, qroma_show_dir


class QromaEditorTypes(str, Enum):
    none = "none"
    root = "root"
    pb = "pb"
    firmware = "firmware"
    app = "app"
    site = "site"


def qroma_open_editor(qroma_project: QromaProject, editor_type: QromaEditorTypes):
    if editor_type == QromaEditorTypes.pb:
        open_pb_editor(qroma_project)
    elif editor_type == QromaEditorTypes.firmware:
        open_firmware_editor(qroma_project)
    elif editor_type == QromaEditorTypes.app:
        open_app_editor(qroma_project)
    elif editor_type == QromaEditorTypes.site:
        open_site_editor(qroma_project)
    elif editor_type == QromaEditorTypes.root:
        qroma_show_dir(qroma_project.project_dir)


def open_pb_editor(qroma_project: QromaProject):
    pb_root = qroma_project.config.qroma.project.dirs.pb_root
    dir_choice = prompt_user_for_dir_choice(pb_root)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_PROTOBUFS.value)


def open_firmware_editor(qroma_project: QromaProject):
    firmware_root = qroma_project.config.qroma.project.dirs.firmware_root
    candidates_dir_path = firmware_root

    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_FIRMWARE.value)


def open_app_editor(qroma_project: QromaProject):
    app_root = qroma_project.config.qroma.project.dirs.app_root
    candidates_dir_path = app_root

    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_APP.value)


def open_site_editor(qroma_project: QromaProject):
    site_root = qroma_project.config.qroma.project.dirs.site_root
    candidates_dir_path = site_root

    dir_choice = prompt_user_for_dir_choice(candidates_dir_path)

    if dir_choice is not None:
        print("OPENING " + dir_choice)
        qroma_edit_dir(dir_choice)
    else:
        raise typer.Exit(ExitReason.UNABLE_TO_EDIT_SITE.value)
