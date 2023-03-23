from commands import toplevel
from commands import pb
from commands import firmware
from commands import app as app_app
from commands import site
from commands import build


app = toplevel.app

app.add_typer(pb.app, name="pb")
app.add_typer(firmware.app, name="firmware")
app.add_typer(app_app.app, name="app")
app.add_typer(site.app, name="site")
app.add_typer(build.app, name="build")


if __name__ == "__main__":
    app()
