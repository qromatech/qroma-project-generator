from commands import toplevel
from commands import pb
from commands import firmware
from commands import app as app_app
from commands import site
from commands import build
from commands import show
from commands import edit
from qroma_infra.qroma_infrastructure import ensure_qroma_user_profile_exists

app = toplevel.app

app.add_typer(pb.app, name="pb")
app.add_typer(firmware.app, name="firmware")
app.add_typer(app_app.app, name="app")
app.add_typer(site.app, name="site")
app.add_typer(build.app, name="build")
app.add_typer(show.app, name="show")
app.add_typer(edit.app, name="edit")


if __name__ == "__main__":
    ensure_qroma_user_profile_exists()
    app()
