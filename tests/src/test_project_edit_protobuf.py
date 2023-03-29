from typer.testing import CliRunner

import pytest

qroma_cli = __import__("qroma-cli")
# from qroma_cli import app


runner = CliRunner()


def test_project_edit_protobuf():
    print("TESTING2")
    result = runner.invoke(qroma_cli.app, ["pb", "edit", ":b"])
    assert result is not None
