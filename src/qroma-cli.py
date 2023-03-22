import typer
from typing import Optional, List

from qroma_project import user_input
from qroma_project.qroma_project import QromaProject, load_qroma_project, load_qroma_project_from_directory
from qroma_types import GenerateProjectOptions, NewQromaProjectInfoFromUserInput, QromaProjectConfigUserInputs
from qroma_enums import FirmwareFramework
# from qroma_project import load_qroma_project, QromaProject, user_input
from typer_validators import \
    typer_validate_new_user_project_id_from_user, \
    typer_validate_existing_project_id_from_user_project_id
from qroma_project.generate.generate_project import do_generate_project_structure
from build_project import do_build_project, create_build_parameters_with_all_steps_disabled, \
    create_build_parameters_with_all_steps_enabled, BuildParameters
from run_project import do_run_project
import env_checks
from qroma_project.generate import project_template
from utils import typer_show_to_user, qroma_show_dir

# from device_boards import DeviceBoardPlatform, DEFAULT_PLATFORMS

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
        firmware_platforms: Optional[List[FirmwareFramework]] = typer.Option(None),
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

    project_config_user_inputs = QromaProjectConfigUserInputs(
        project_info,
        firmware_platforms=firmware_platforms
    )
    # project_config = create_project_config_from_user_inputs(project_config_user_inputs)
    #
    # new_qp = QromaProject(project_info.project_dir, project_info.project_id)
    # new_qp.set_config(project_config)

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

    # this_project: QromaProject = QromaProject(project_info.project_dir, project_id)
    # this_project.set_config(project_config)

    do_build_project(qroma_project=this_project,
                     build_parameters=generate_project_options.build_parameters,
                     )

    qroma_show_dir(this_project.project_dir)

    typer_show_to_user(f"Done initializing Qroma project: {project_id}")


@app.command()
def protobuf(project_id: str = typer.Argument(None,
                                              # callback=typer_validate_existing_project_id_from_user_project_id,
                                              ),
             ):
    """
    Compile Protocol Buffer definitions for this project. Provide no arguments to compile Protobufs for the project in
    the current directory. Use '#' before the project_id to compile a project in the global 'qroma-projects' directory.
    """
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)

    typer_show_to_user(f"Compiling protocol buffers for {qroma_project.project_id}")

    build_parameters = create_build_parameters_with_all_steps_disabled()
    build_parameters.include_pb = True

    do_build_project(qroma_project, build_parameters)

    typer_show_to_user(f"Done compiling protocol buffers for {qroma_project.project_id}")


@app.command()
def build(project_id: Optional[str] = typer.Argument(None,
                                                     # callback=typer_validate_existing_project_id_from_user_project_id
                                                     ),
          pb: bool = typer.Option(False, help="Compile protobufs as part of build (equivalent to running 'protobuf')."),
          ):
    """
    Build Qroma software for this project. Provide no arguments to build the Qroma project in
    the current directory. Use '#' before the project_id to build a project in the global 'qroma-projects' directory.
    """
    # qroma_project = project_template.get_qroma_project_for_user_supplied_project_id(project_id)
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)

    typer_show_to_user("Building Qroma software")

    build_parameters = create_build_parameters_with_all_steps_enabled()
    build_parameters.include_pb = pb

    do_build_project(qroma_project, build_parameters)

    typer_show_to_user("Done building Qroma software")


@app.command()
def run(project_id: Optional[str] = typer.Argument(None,
                                                   callback=typer_validate_existing_project_id_from_user_project_id,
                                                   # callback=create_typer_coercion_fn(),
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


@app.command()
def dir(project_id: Optional[str] = typer.Argument(None,
                                                   callback=typer_validate_existing_project_id_from_user_project_id,
                                                   ),
        ):
    """
    Open the supplied project_id Qroma project directory in an Explorer or Finder window.
    """
    qroma_project_info = project_template.get_qroma_project_info_from_user(project_id)
    qroma_show_dir(qroma_project_info.project_dir)


@app.command()
def show(project_id: Optional[str] = typer.Argument(None,
                                                    callback=typer_validate_existing_project_id_from_user_project_id,
                                                    ),
         ):
    """
    Show the supplied project_id Qroma config.
    """
    qroma_project_info = project_template.get_qroma_project_info_from_user(project_id)
    qroma_config = load_qroma_project(qroma_project_info)
    typer_show_to_user(f"{qroma_config}")


# @app.command()
# def jt(project_id: Optional[str] = typer.Argument(None,
#                                                   callback=typer_validate_new_user_project_id_from_user,
#                                                   ),
#        dev_board_platforms: Optional[List[DeviceBoardPlatform]] = typer.Option(None),
#        replace_existing: bool = typer.Option(False),
#        do_build: bool = typer.Option(False),
#        build_ignore_www: bool = typer.Option(True),
#        ):
#     """
#     """
#     project_info = project_template.create_new_qroma_project_info_from_user_input(project_id)
#     if os.path.exists(project_info.project_dir):
#         if not replace_existing:
#             typer_show_to_user(f"Project ID {project_info.project_id} already created. See {project_info.project_dir}.\n"
#                                "  Add --replace-existing if you want to delete the existing project.")
#             raise typer.Exit()
#         # qroma_os_rmdir(new_qp.project_dir)
#
#     # qroma_project = QromaProject()
#     # logging.info(f"PROJECT ROOT DIR: {qroma_project.project_root_dir}")
#
#     typer_show_to_user(f"Initializing Qroma project: {project_info.project_id}")
#
#     project_config = QromaProjectConfig(
#         dev_board_platforms=dev_board_platforms
#     )
#
#     new_qp = QromaProject(project_info.project_dir, project_info.project_id)
#     new_qp.set_config(project_config)
#
#     build_parameters = BuildParameters(
#         include_pb=do_build,
#         include_device=do_build,
#         include_site=do_build and not build_ignore_www,
#     )
#
#     generate_project_options = GenerateProjectOptions(
#         project_config=project_config,
#         build_parameters=build_parameters,
#         replace_existing_project_directory=replace_existing,
#     )
#
#     do_generate_project(new_qp, generate_project_options)
#     qroma_show_dir(new_qp.project_dir)
#
#     typer_show_to_user(f"Done initializing Qroma project: {project_id}")


if __name__ == "__main__":
    app()
