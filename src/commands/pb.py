from typing import Optional

import typer

from qroma_infra.qroma_editor import open_pb_editor
from qroma_project import user_input
from steps import pb_steps

app = typer.Typer(help="Qroma protocol buffer management commands")


@app.command()
def clean(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    pb_steps.run_pb_clean_step(qroma_project)


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_pb_editor(qroma_project)


@app.command(name="compile")
def pb_compile(project_id: Optional[str] = typer.Argument(None)):
    """
    Compile Protocol Buffer definitions for this project. Provide no arguments to compile Protobufs for the project in
    the current directory. Use ':' before the project_id to compile a project in the global 'qroma-projects' directory.
    """
    try:
        qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
        pb_steps.run_pb_compile_step(qroma_project)
    except Exception as e:
        print(f"Error compiling PB: {e}")


@app.command()
def install(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    pb_steps.run_pb_install_step(qroma_project)


@app.command()
def build(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    pb_steps.run_pb_build_step(qroma_project)
