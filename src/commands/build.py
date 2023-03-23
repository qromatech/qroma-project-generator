import typer

app = typer.Typer(help="Qroma project build management commands")


@app.command(name="all")
def build_all():
    print("In build all - not yet implemented")


@app.command()
def firmware():
    print("In build firmware - not yet implemented")


@app.command(name="app")
def build_app():
    print("In build app - not yet implemented")


@app.command()
def site():
    print("In build site - not yet implemented")
