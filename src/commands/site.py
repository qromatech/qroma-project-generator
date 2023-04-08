from typing import Optional

import typer

from qroma_infra.qroma_editor import open_site_editor
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input
from steps.site import site_build
from steps.site.site_bundle import do_site_bundle_work

app = typer.Typer(help="Qroma site management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_site_editor(qroma_project)


@app.command()
def bundle(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    do_site_bundle_work(qroma_project)


@app.command()
def run(project_id: Optional[str] = typer.Argument(None)):
    print("In site run - not yet implemented")


@app.command()
def build(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    site_build.do_full_site_build(qroma_project, user_profile)
