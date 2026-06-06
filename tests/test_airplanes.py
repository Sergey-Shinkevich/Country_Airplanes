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
