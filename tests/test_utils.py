from typing import List

import pytest

from src.airplanes import Airplane
from src.utils import filter_airplanes, sort_airplanes


@pytest.fixture
def sample_airplanes() -> List[Airplane]:
    """Фикстура для создания тестового списка самолетов"""
    return [
        Airplane("AIR1", "Russia", "Test", 100.0, 5000.0),
        Airplane("AIR2", "USA", "Test", 200.0, 10000.0),
        Airplane("AIR3", "Russia", "Test", 150.0, 7000.0),
    ]


def test_filter_airplanes(sample_airplanes: List[Airplane]) -> None:
    """Тест фильтрации самолетов по стране регистрации"""
    filtered = filter_airplanes(sample_airplanes, "Russia")
    assert len(filtered) == 2
    assert all(a.country == "Russia" for a in filtered)


def test_sort_airplanes(sample_airplanes: List[Airplane]) -> None:
    """Тест сортировки"""
    sorted_data = sort_airplanes(sample_airplanes)
    assert sorted_data[0].geo_altitude == 10000.0
    assert sorted_data[1].geo_altitude == 7000.0
    assert sorted_data[2].geo_altitude == 5000.0


def test_sort_empty_list() -> None:
    """Тест пустого списка"""
    assert sort_airplanes([]) == []
