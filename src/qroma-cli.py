import logging
import typer
from typing import Optional, List

from qroma_project_config import QromaProjectConfig
from qroma_types import GenerateProjectOptions
from qroma_enums import DeviceBoardPlatform
from qroma_project import does_qroma_project_dir_exist
from typer_validators import typer_validate_new_project_id, typer_validate_existing_project_id
from generate_project import do_generate_project
from build_project import do_build_project, create_build_parameters_with_all_steps_disabled,\
    create_build_parameters_with_all_steps_enabled
from run_project import do_run_project
import env_checks
import project_template
from utils import typer_show_to_user, qroma_os_remove

# from device_boards import DeviceBoardPlatform, DEFAULT_PLATFORMS

app = typer.Typer(help="Qroma project manager for the command line")


@app.command()
def env():
    typer_show_to_user("Checking your system for tools used by Qroma to build your project...")
    env_checks.do_env_checks()


@app.command()
def new(project_id: str = typer.Argument(...,
                                         callback=typer_validate_new_project_id,
                                         # callback=typer_validate_existing_project_id,
                                         ),
        dev_board_platforms: Optional[List[DeviceBoardPlatform]] = typer.Option(None),
        replace_existing: bool = typer.Option(False),
        ):
    """
    Initialize a new Qroma project. Give a project ID to create a new project in this directory. If you
    prefix the project ID with ':', it will create your project in a global 'qroma-projects' directory.
    """
    new_qp = project_template.get_qroma_project_for_user_supplied_project_id(project_id)
    if does_qroma_project_dir_exist(new_qp):
        if not replace_existing:
            typer_show_to_user(f"Project ID {new_qp.project_id} already created. See {new_qp.project_dir}.")
            raise typer.Exit()
        qroma_os_remove(new_qp.project_dir)

    logging.info(f"PROJECT ROOT DIR: {new_qp.project_root_dir}")

    typer_show_to_user(f"Initializing Qroma project: {project_id}")

    project_config = QromaProjectConfig(
        dev_board_platforms=dev_board_platforms
    )

    generate_project_options = GenerateProjectOptions(project_config=project_config)
    do_generate_project(new_qp, generate_project_options)

    typer_show_to_user(f"Done initializing Qroma project: {project_id}")


@app.command()
def protobuf(project_id: Optional[str] = typer.Argument(None,
                                                        callback=typer_validate_existing_project_id
                                                        )):
    """
    Compile Protocol Buffer definitions for this project. Provide no arguments to compile Protobufs for the project in
    the current directory. Use '#' before the project_id to compile a project in the global 'qroma-projects' directory.
    """
    qroma_project = project_template.get_qroma_project_for_user_supplied_project_id(project_id)

    typer_show_to_user(f"Compiling protocol buffers for {qroma_project.project_id}")

    build_parameters = create_build_parameters_with_all_steps_disabled()
    build_parameters.include_pb = True

    do_build_project(qroma_project, build_parameters)

    typer_show_to_user(f"Done compiling protocol buffers for {qroma_project.project_id}")


@app.command()
def build(project_id: Optional[str] = typer.Argument(None,
                                                     callback=typer_validate_existing_project_id
                                                     ),
          pb: bool = typer.Option(False, help="Compile protobufs as part of build (equivalent to running 'pb')."),
          ):
    """
    Build Qroma software for this project. Provide no arguments to build the Qroma project in
    the current directory. Use '#' before the project_id to build a project in the global 'qroma-projects' directory.
    """
    qroma_project = project_template.get_qroma_project_for_user_supplied_project_id(project_id)

    typer_show_to_user("Building Qroma software")

    build_parameters = create_build_parameters_with_all_steps_enabled()
    build_parameters.include_pb = pb

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
