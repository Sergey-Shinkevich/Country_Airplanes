from src.airplanes import Airplane


def test_airplanes_init_full() -> None:
    """Проверка корректной инициализации со всеми данными"""
    plane = Airplane("123456", "Canada", "ACA123", 500.0, 10000.0)
    assert plane.icao24 == "123456"
    assert plane.callsign == "ACA123"
    assert plane.velocity == 500.0


def test_airplanes_init_missing_callsign() -> None:
    """Проверка создания позывного, если передан None"""
    # 123 + Canada = "123Canada"
    plane = Airplane("123456", "Canada", None, 500.0, 10000.0)
    assert plane.callsign == "123Canada"


def test_comparisons() -> None:
    """Проверка методов сравнения"""
    plane_slow = Airplane("1", "A", "C1", 100.0, 1000.0)
    plane_fast = Airplane("2", "B", "C2", 200.0, 2000.0)

    # Проверка __lt__ (меньше)
    assert plane_slow < plane_fast
    # Проверка __gt__ (больше)
    assert plane_fast > plane_slow
    # Проверка __le__ (меньше или равно)
    assert plane_slow <= plane_fast
    assert plane_slow <= plane_slow


def test_airplanes_init_none_values() -> None:
    """Проверка инициализации при отсутствии скорости и высоты"""
    plane = Airplane("123", "USA", "A1", None, None)
    assert plane.velocity == 0.0
    assert plane.geo_altitude == 0.0


def test_cast_to_object_list() -> None:
    """Проверка превращения JSON в список объектов"""
    mock_json = {
        "states": [
            ["icao1", "callsign1", "Country1", None, None, None, None, 1000.0, None, 500.0],
            ["icao2", "callsign2", "Country2", None, None, None, None, 2000.0, None, 600.0],
        ]
    }

    planes = Airplane.cast_to_object_list(mock_json)

    assert len(planes) == 2
    assert isinstance(planes[0], Airplane)

    assert planes[0].callsign == "callsign1"
    assert planes[0].geo_altitude == 1000.0
    assert planes[1].velocity == 600.0


def test_cast_to_object_list_empty() -> None:
    """Проверка, что метод не падает при пустых данных"""
    assert Airplane.cast_to_object_list({}) == []
    assert Airplane.cast_to_object_list({"states": None}) == []
