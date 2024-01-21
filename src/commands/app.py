from typing import Optional

import typer

from qroma_infra.qroma_editor import open_app_editor
from qroma_project import user_input


app = typer.Typer(help="Qroma app management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_app_editor(qroma_project)


@app.command()
def build():
    print("In app build - not yet implemented."
          " See https://stackoverflow.com/questions/4537411/compile-but-do-not-run-a-python-script")


@app.command()
def run():
    print("In app run - not yet implemented")
