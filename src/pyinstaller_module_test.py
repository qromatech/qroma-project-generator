import typer

import mod1.imp1


app = typer.Typer(help="Pyinstaller test - Qroma project manager for the command line")

mod1.imp1.imp1_exe("xyz")


@app.command()
def env():
    """
    Check your environment for tools that the Qroma CLI might require.
    """
    print("Doing env check")


@app.command()
def new(project_id: str):
    """
    Initialize a new Qroma project. Give a project ID to create a new project in this directory. If you
    prefix the project ID with ':', it will create your project in a global 'qroma-projects' directory.
    """
    print(f"Initializing {project_id}")


if __name__ == "__main__":
    app()
