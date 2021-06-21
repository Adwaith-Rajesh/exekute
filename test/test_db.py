import json
import os
from pathlib import Path

import pytest

from exekute.core.db import DataBase

test_data = {
    "3425345": {
        "name": "project1",
                "apps": ["test.exe", "name.exe"],
                "script": ""
    },
    "123456": {
        "name": "project2",
                "apps": ["p.exe", "n.exe"],
                "script": "test.bat"
    },
}


@pytest.fixture
def json_file():
    with open("test.json", "w") as f:
        json.dump(test_data, f)
    yield "test.json"
    os.remove("test.json")


def test_database_get_all(json_file: str, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    a = DataBase()
    assert a.get_all() == test_data


def test_database_get_by_id(json_file: str, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    a = DataBase()
    assert a.get_by_id("3425345") == test_data["3425345"]


def test_database_add_no_id_exists(json_file, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    a = DataBase()
    demo_data = {"name": "project2", "apps": ["te.exe"], "script": "hello.bat"}
    a.add("098765", demo_data)

    with open(json_file, "r") as f:
        data = json.load(f)
        assert data["098765"] == demo_data
        assert len(data) == 3


def test_database_add_id_exists(json_file, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    a = DataBase()
    demo_data = {"name": "project2", "apps": ["te.exe"], "script": "hello.bat"}
    a.add("123456", demo_data)

    with open(json_file, "r") as f:
        data = json.load(f)
        assert data["123456"] == demo_data
        assert len(data) == 2


def test_database_file_not_exist(mocker) -> None:
    mocker.patch("os.path.join", return_value="test.json")
    _ = DataBase()
    assert Path("test.json").is_file() is True


def test_database_json_decode_error(json_file: str, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    with open(json_file, "w") as f:
        f.write("")
    _ = DataBase()

    with open(json_file, "r") as f:
        assert f.read() == "{}"


def test_database_del_by_id(json_file: str, mocker) -> None:
    mocker.patch("os.path.join", return_value=json_file)
    a = DataBase()

    with open(json_file, "r") as f:
        data = json.load(f)
    assert len(data) == 2
    a.del_by_id("123456")
    with open(json_file, "r") as f:
        data = json.load(f)
    assert len(data) == 1
