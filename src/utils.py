def filter_airplanes(airplanes: list, country_name: str) -> list:
    """Фильтрует список самолетов по стране регистрации."""
    return [a for a in airplanes if a.country == country_name]


def sort_airplanes(airplanes: list) -> list:
    """Сортирует список самолетов по высоте (по убыванию)."""
    return sorted(airplanes, reverse=True)


def get_top_airplanes(airplanes: list, top_n: int) -> list:
    """Возвращает топ N самолетов."""
    return airplanes[:top_n]


def print_airplanes(airplanes: list) -> None:
    """Выводит список самолетов в удобном виде."""
    for a in airplanes:
        print(f"Callsign: {a.callsign}, Высота: {a.geo_altitude}, Страна: {a.country}")
