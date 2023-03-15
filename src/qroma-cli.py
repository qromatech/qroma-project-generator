import os
import typer
from typing import Optional

from typer_project_generator import typer_validate_new_project_id, typer_validate_existing_project_id
from generate_project import do_generate_project
from compile_protobuf import do_compile_protobuf
from build_project import do_build_project
from run_project import do_run_project
import env_checks

app = typer.Typer(help="Qroma project manager for the command line")


@app.command()
def env():
    print("Checking your system for tools used by Qroma to build your project...")
    env_checks.do_env_checks()


@app.command()
def init(project_id: str = typer.Argument(...,
                                          # prompt="Enter a project ID",
                                          callback=typer_validate_new_project_id
                                          ),
         ):
    """
    Initialize a new Qroma project.
    """
    project_root_dir = os.getcwd()
    print(f"PROJECT ROOT DIR: {project_root_dir}")

    print(f"Initializing Qroma project: {project_id}")
    do_generate_project(project_id, project_root_dir)
    print(f"Done initializing Qroma project: {project_id}")


@app.command()
def pb(project_id: Optional[str] = typer.Argument(None,
                                                  callback=typer_validate_existing_project_id
                                                  )):
    """
    Compile Protocol Buffer definitions for this project.
    """
    print(f"Compiling protocol buffers for {project_id}")
    do_compile_protobuf(project_id)
    print(f"Done compiling protocol buffers for {project_id}")


@app.command()
def build(project_id: Optional[str] = typer.Argument(None,
                                                     callback=typer_validate_existing_project_id
                                                     )):
    """
    Build Qroma software associated with this project.
    """
    print("Building Qroma software")
    pb(project_id)
    do_build_project(project_id)
    print("Done building Qroma software")


@app.command()
def run(project_id: Optional[str] = typer.Argument(None,
                                                   callback=typer_validate_existing_project_id
                                                   )):
    """
    Build, install, and run Qroma software associated with this project.
    """
    print("Starting up Qroma software")
    do_run_project(project_id)
    print("Qroma software is running")


@app.command()
def publish():
    """
    Publish Qroma software for this project.
    """
    print("Publishing Qroma software")
    exit("Publish has not been implemented")


if __name__ == "__main__":
    app()
