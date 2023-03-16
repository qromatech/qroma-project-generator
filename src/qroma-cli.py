import logging
import typer
from typing import Optional

from typer_validators import typer_validate_new_project_id, typer_validate_existing_project_id
from generate_project import do_generate_project
from compile_protobuf import do_compile_protobuf
from build_project import do_build_project
from run_project import do_run_project
import env_checks
import project_template
from utils import typer_show_to_user

app = typer.Typer(help="Qroma project manager for the command line")


@app.command()
def env():
    typer_show_to_user("Checking your system for tools used by Qroma to build your project...")
    env_checks.do_env_checks()


@app.command()
def new(project_id: str = typer.Argument(...,
                                         callback=typer_validate_new_project_id,
                                         )):
    """
    Initialize a new Qroma project. Give a project ID to create a new project in this directory. If you
    prefix the project ID with ':', it will create your project in a global 'qroma-projects' directory.
    """
    new_qp = project_template.get_qroma_project_for_user_supplied_project_id(project_id)
    logging.info(f"PROJECT ROOT DIR: {new_qp.project_root_dir}")

    typer_show_to_user(f"Initializing Qroma project: {project_id}")
    do_generate_project(new_qp.project_id, new_qp.project_root_dir)
    typer_show_to_user(f"Done initializing Qroma project: {project_id}")


@app.command()
def pb(project_id: Optional[str] = typer.Argument(None,
                                                  callback=typer_validate_existing_project_id
                                                  )):
    """
    Compile Protocol Buffer definitions for this project. Provide no arguments to compile Protobufs for the project in
    the current directory. Use '#' before the project_id to compile a project in the global 'qroma-projects' directory.
    """
    qroma_project = project_template.get_qroma_project_for_user_supplied_project_id(project_id)

    typer_show_to_user(f"Compiling protocol buffers for {qroma_project.project_id}")
    do_compile_protobuf(qroma_project)
    typer_show_to_user(f"Done compiling protocol buffers for {qroma_project.project_id}")


@app.command()
def build(project_id: Optional[str] = typer.Argument(None,
                                                     callback=typer_validate_existing_project_id
                                                     )):
    """
    Build Qroma software for this project. Provide no arguments to build the Qroma project in
    the current directory. Use '#' before the project_id to build a project in the global 'qroma-projects' directory.
    """
    qroma_project = project_template.get_qroma_project_for_user_supplied_project_id(project_id)

    typer_show_to_user("Building Qroma software")
    pb(project_id)
    do_build_project(qroma_project)
    typer_show_to_user("Done building Qroma software")


@app.command()
def run(project_id: Optional[str] = typer.Argument(None,
                                                   callback=typer_validate_existing_project_id
                                                   )):
    """
    Build, install, and run Qroma software associated with this project.
    """
    typer_show_to_user("Starting up Qroma software")
    do_run_project(project_id)
    typer_show_to_user("Qroma software is running")


@app.command()
def publish():
    """
    Publish Qroma software for this project.
    """
    typer_show_to_user("Publishing Qroma software")
    typer_show_to_user("Publish has not been implemented")


if __name__ == "__main__":
    app()
