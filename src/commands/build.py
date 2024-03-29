from typing import Optional

import typer

from build_project import do_build_project, BuildParameters
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input

app = typer.Typer(help="Qroma project build management commands")


# @app.command(name="all")
@app.callback(invoke_without_command=True)
def build_all(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    build_parameters = BuildParameters(
        build_pb=True,
        build_firmware=True,
        build_site=True,
    )

    do_build_project(qroma_project=qroma_project,
                     user_profile=user_profile,
                     build_parameters=build_parameters,
                     )


@app.command()
def pb(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    build_parameters = BuildParameters(
        build_pb=True,
        build_firmware=False,
        build_site=False,
    )

    do_build_project(qroma_project=qroma_project,
                     user_profile=user_profile,
                     build_parameters=build_parameters,
                     )


@app.command()
def firmware(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    build_parameters = BuildParameters(
        build_pb=False,
        build_firmware=True,
        build_site=False,
    )

    do_build_project(qroma_project=qroma_project,
                     user_profile=user_profile,
                     build_parameters=build_parameters,
                     )


@app.command(name="app")
def build_app(project_id: Optional[str] = typer.Argument(None)):
    print("In build app - not yet implemented")


@app.command()
def site(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    build_parameters = BuildParameters(
        build_pb=False,
        build_firmware=False,
        build_site=True,
    )

    do_build_project(qroma_project=qroma_project,
                     user_profile=user_profile,
                     build_parameters=build_parameters,
                     )
