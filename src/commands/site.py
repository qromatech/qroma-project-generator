import typer

app = typer.Typer(help="Qroma site management commands")


@app.command()
def edit():
    print("In site edit - not yet implemented")


@app.command()
def build():
    print("In site build - not yet implemented")


@app.command()
def run():
    print("In site run - not yet implemented")
