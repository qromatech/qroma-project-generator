
import pytest

qroma_cli = __import__("qroma-cli")


def test_project_compile_protobuf():
    project_id = ":x"
    qroma_cli.protobuf(project_id)

    print("hello world")
    assert True
