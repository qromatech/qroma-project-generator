import typer


app = typer.Typer(help="Qroma app management commands")


@app.command()
def edit():
    print("In app edit - not yet implemented")


@app.command()
def build():
    print("In app build - not yet implemented."
          " See https://stackoverflow.com/questions/4537411/compile-but-do-not-run-a-python-script")


@app.command()
def run():
    print("In app run - not yet implemented")
