import typer


app = typer.Typer(help="Qroma firmware management commands")


@app.command()
def edit():
    print("In firmware edit - not yet implemented")


@app.command()
def build():
    print("In firmware build - not yet implemented")


@app.command()
def upload():
    print("In firmware upload - not yet implemented")


# @app.command()
# def build(project_id: Optional[str] = typer.Argument(None,
#                                                      # callback=typer_validate_existing_project_id_from_user_project_id
#                                                      ),
#           pb: bool = typer.Option(False, help="Compile protobufs as part of build (equivalent to running 'protobuf')."),
#           ):
#     """
#     Build Qroma software for this project. Provide no arguments to build the Qroma project in
#     the current directory. Use ':' before the project_id to build a project in the global 'qroma-projects' directory.
#     """
#     qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
#
#     typer_show_to_user("Building Qroma software")
#
#     build_parameters = create_build_parameters_with_all_steps_enabled()
#     build_parameters.include_pb = pb
#
#     do_build_project(qroma_project, build_parameters)
#
#     typer_show_to_user("Done building Qroma software")