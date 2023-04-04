from typing import Optional

import typer

from qroma_project import user_input
from qroma_infra.qroma_editor import open_firmware_editor, open_app_editor, open_site_editor, open_pb_editor

app = typer.Typer(help="Qroma software editor commands")


@app.command()
def pb(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_pb_editor(qroma_project)


@app.command()
def firmware(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_firmware_editor(qroma_project)


@app.command(name="app")
def edit_app(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_app_editor(qroma_project)


@app.command()
def site(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_site_editor(qroma_project)
