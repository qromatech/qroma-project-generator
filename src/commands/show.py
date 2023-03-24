from typing import Optional

import typer

from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input

app = typer.Typer(help="Look at configurations used by Qroma")


@app.command()
def project(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    print(qroma_project.config)


@app.command()
def user():
    qroma_user_profile = load_qroma_user_profile()
    print(qroma_user_profile)
