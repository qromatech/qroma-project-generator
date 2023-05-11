from typing import List

import typer

import env_checks
from build_project import BuildParameters, do_build_project
from qroma_infra.qroma_editor import QromaEditorTypes, qroma_open_editor
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
        # firmware_platforms: List[FirmwareFramework] | None = typer.Option(None),
        editor: QromaEditorTypes = typer.Option(QromaEditorTypes.root),
        replace_existing: bool = typer.Option(False),
        do_build: bool = typer.Option(False),
        build_ignore_www: bool = typer.Option(True),
        full_build: bool = typer.Option(False),
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

    user_firmware_platform = user_profile.defaults.new_project_firmware_platform
    typer_show_to_user(f"Using user preference to create firmware framework: {user_firmware_platform}.")

    project_config_user_inputs = QromaProjectConfigUserInputs(
        project_info,
        firmware_platform=user_firmware_platform
    )

    build_parameters = BuildParameters(
        build_pb=do_build or full_build,
        build_firmware=do_build or full_build,
        build_site=(do_build and not build_ignore_www) or full_build,
    )

    generate_project_options = GenerateProjectOptions(
        project_config_user_inputs=project_config_user_inputs,
        build_parameters=build_parameters,
        replace_existing_project_directory=replace_existing,
    )

    do_generate_project_structure(generate_project_options)

    this_project = load_qroma_project_from_directory(project_info.project_dir)
    user_profile = load_qroma_user_profile()

    do_build_project(qroma_project=this_project,
                     user_profile=user_profile,
                     build_parameters=generate_project_options.build_parameters,
                     )

    qroma_open_editor(this_project, editor)

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
