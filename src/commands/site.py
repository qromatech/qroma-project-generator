from typing import Optional

import typer

from qroma_infra.qroma_editor import open_site_editor
from qroma_project import user_input

app = typer.Typer(help="Qroma site management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_site_editor(qroma_project)


@app.command()
def build(project_id: Optional[str] = typer.Argument(None)):
    print("In site build - not yet implemented")


@app.command()
def run(project_id: Optional[str] = typer.Argument(None)):
    print("In site run - not yet implemented")
