
import pytest

qroma_cli = __import__("qroma-cli")


def test_create_new_project():
    project_id = ":x"
    qroma_cli.new(project_id,
                  dev_board_platforms=['arduino'],
                  replace_existing=True,
                  do_build=False,
                  build_ignore_www=False,
                  )

    print("hello world")
    assert True
