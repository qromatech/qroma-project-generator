
import pytest

qroma_cli = __import__("qroma-cli")


def test_project_build():
    project_id = ":x"
    qroma_cli.build(project_id, pb=False)

    print("hello world")
    assert True
