import typer


app = typer.Typer(help="Qroma protocol buffer management commands")


@app.command()
def edit():
    print("In pb edit - not yet implemented")


@app.command(name="compile")
def pb_compile():
    print("In pb compile - not yet implemented")


@app.command()
def install():
    print("In pb install - not yet implemented")


@app.command()
def build():
    print("In pb build - not yet implemented")



# @app.command()
# def protobuf(project_id: str = typer.Argument(None,
#                                               # callback=typer_validate_existing_project_id_from_user_project_id,
#                                               ),
#              ):
#     """
#     Compile Protocol Buffer definitions for this project. Provide no arguments to compile Protobufs for the project in
#     the current directory. Use '#' before the project_id to compile a project in the global 'qroma-projects' directory.
#     """
#     qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
#
#     typer_show_to_user(f"Compiling protocol buffers for {qroma_project.project_id}")
#
#     build_parameters = create_build_parameters_with_all_steps_disabled()
#     build_parameters.include_pb = True
#
#     do_build_project(qroma_project, build_parameters)
#
#     typer_show_to_user(f"Done compiling protocol buffers for {qroma_project.project_id}")