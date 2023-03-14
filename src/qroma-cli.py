import os
import typer
from generate_project import do_generate_project
from typer_project_generator import typer_validate_new_project_id, typer_validate_existing_project_id
from compile_protobuf import do_compile_protobuf
from typing import Optional

from build_project import do_build_project
from qroma_project import load_current_dir_qroma_project


app = typer.Typer(help="Qroma project manager for the command line")


@app.command()
def init(project_id: str = typer.Argument(...,
                                          # prompt="Enter a project ID",
                                          callback=typer_validate_new_project_id
                                          ),
         # project_root_dir: str = typer.Option("",
         #                                      prompt="Enter the parent directory for the project",
         #                                      callback=typer_validate_project_root_dir,
         #                                      ),
         ):
    """
    Initialize a new Qroma project.
    """
    # validated_project_id = validate_project_id(project_id)
    # if validated_project_id == "":
    #     raise typer.BadParameter(f"Invalid project ID value: {project_id}")
    #
    # if project_root_dir.strip() == '.':
    #     print("USE CWD")
    #     project_root_dir = os.getcwd()
    # elif project_root_dir.strip() == '':
    #     print("USE DEFAULT")
    #     project_root_dir = QROMA_DEFAULT_PROJECT_ROOT_DIR
    # validated_project_root_dir = validate_project_root_dir(project_root_dir)

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
def build():
    """
    Build Qroma software associated with this project.
    """
    print("Building Qroma software")
    do_build_project()
    print("Done building Qroma software")


@app.command()
def publish():
    """
    Publish Qroma software for this project.
    """
    print("Publishing Qroma software")


if __name__ == "__main__":
    app()
