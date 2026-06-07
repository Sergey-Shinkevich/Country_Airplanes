from typing import Any

import pytest

from src.airplanes import Airplane
from src.file_operation import JSONSaver


@pytest.fixture
def temp_file(tmp_path: Any) -> Any:
    """Фикстура для создания временного файла"""
    return tmp_path / "test_data.json"


def test_save_and_get_all(temp_file: Any) -> None:
    """Проверка записи и чтения"""
    saver = JSONSaver(str(temp_file))
    plane = Airplane("123", "Canada", "ACA123", 500.0, 10000.0)
    saver.save_all([plane])
    loaded = saver.get_all()

    assert len(loaded) == 1
    assert loaded[0].icao24 == "123"


def test_delete_airplane(temp_file: Any) -> None:
    """Проверка удаления самолета"""
    saver = JSONSaver(str(temp_file))
    plane1 = Airplane("1", "A", "C1", 100.0, 1000.0)
    plane2 = Airplane("2", "B", "C2", 200.0, 2000.0)

    saver.save_all([plane1, plane2])
    saver.delete_airplane("1")

    loaded = saver.get_all()
    assert len(loaded) == 1
    assert loaded[0].icao24 == "2"


def test_get_all_empty_file() -> None:
    """Проверка, что пустой/несуществующий файл не вызывает крах"""
    saver = JSONSaver("non_existent.json")
    assert saver.get_all() == []
