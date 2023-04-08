from typing import Optional

import typer

from qroma_infra.qroma_editor import open_firmware_editor
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input
from steps import firmware_steps


app = typer.Typer(help="Qroma firmware management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_firmware_editor(qroma_project)


@app.command()
def build(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    firmware_steps.run_firmware_build_step(qroma_project, user_profile)


@app.command()
def upload(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    firmware_steps.run_firmware_upload_step(qroma_project, user_profile)
