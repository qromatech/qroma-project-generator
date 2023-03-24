from typing import List

import typer

import env_checks
from build_project import BuildParameters, do_build_project
from qroma_enums import FirmwareFramework
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input
from qroma_project.generate.generate_project import do_generate_project_structure
from qroma_project.qp_loader import load_qroma_project_from_directory
from qroma_types import QromaProjectConfigUserInputs, GenerateProjectOptions
from utils import typer_show_to_user, qroma_show_dir

app = typer.Typer(help="Qroma project manager for the command line")


@app.command()
def env():
    """
    Check your environment for tools that the Qroma CLI might require.
    """
    typer_show_to_user("Checking your system for tools used by Qroma to build your project...")
    env_checks.do_env_checks()


@app.command()
def new(project_id: str = typer.Argument(...,
                                         # callback=typer_validate_new_user_project_id_from_user,
                                         # callback=typer_validate_existing_project_id,
                                         ),
        firmware_platforms: List[FirmwareFramework] | None = typer.Option(None),
        replace_existing: bool = typer.Option(False),
        do_build: bool = typer.Option(False),
        build_ignore_www: bool = typer.Option(True),
        ):
    """
    Initialize a new Qroma project. Give a project ID to generate a new project in this directory. If you
    prefix the project ID with ':', it will generate your project in a global 'qroma-projects' directory.
    """
    project_info = user_input.create_new_qroma_project_info_from_user_input(project_id)

    if project_info.project_dir_exists and not replace_existing:
        typer_show_to_user(f"Project ID {project_info.project_id} already created. See {project_info.project_dir}.\n"
                           "  Add --replace-existing if you want to delete the existing project.")
        raise typer.Exit()

    typer_show_to_user(f"Initializing Qroma project: {project_info.project_id}")

    user_profile = load_qroma_user_profile()

    if not firmware_platforms:
        user_firmware_platforms = user_profile.defaults.preferences.firmware_platforms
        typer_show_to_user(f"No firmware platforms provided. Using user preferences [{user_firmware_platforms}].")
    else:
        user_firmware_platforms = firmware_platforms

    project_config_user_inputs = QromaProjectConfigUserInputs(
        project_info,
        firmware_platforms=user_firmware_platforms
    )

    build_parameters = BuildParameters(
        include_pb=do_build,
        include_device=do_build,
        include_site=do_build and not build_ignore_www,
    )

    generate_project_options = GenerateProjectOptions(
        project_config_user_inputs=project_config_user_inputs,
        build_parameters=build_parameters,
        replace_existing_project_directory=replace_existing,
    )

    do_generate_project_structure(generate_project_options)

    this_project = load_qroma_project_from_directory(project_info.project_dir)

    do_build_project(qroma_project=this_project,
                     build_parameters=generate_project_options.build_parameters,
                     )

    qroma_show_dir(this_project.project_dir)

    typer_show_to_user(f"Done initializing Qroma project: {project_id}")


def version_callback(value: bool):
    if value:
        import version_info
        version = version_info.get_version()
        typer.echo(f"Qroma CLI Version: {version}")
        raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass
