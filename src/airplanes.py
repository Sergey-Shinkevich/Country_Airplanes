from typing import Any


class Airplane:
    def __init__(self, icao24: Any, country: Any, callsign: Any, velocity: Any, geo_altitude: Any):
        """Конструктор класса Airplanes"""
        self.icao24 = icao24
        self.country = country
        self.callsign = (icao24[0:3] + country) if callsign.strip() in [None, ""] else callsign
        self.velocity = float(velocity) if velocity is not None else 0.0
        self.geo_altitude = float(geo_altitude) if geo_altitude is not None else 0.0

    def __lt__(self, other: Airplane) -> Any:
        return self.velocity < other.velocity and self.geo_altitude < other.geo_altitude

    def __le__(self, other: Airplane) -> Any:
        return self.velocity <= other.velocity and self.geo_altitude <= other.geo_altitude

    def __gt__(self, other: Airplane) -> Any:
        return self.velocity > other.velocity and self.geo_altitude > other.geo_altitude

    def __ge__(self, other: Airplane) -> Any:
        return self.velocity >= other.velocity and self.geo_altitude >= other.geo_altitude

    @staticmethod
    def cast_to_object_list(raw_data: dict) -> list[Airplane]:
        """
        Превращает JSON-ответ от API в список объектов Airplane.
        raw_data — это словарь, который возвращает OpenSky (ключ 'states')
        """
        if not raw_data or "states" not in raw_data or raw_data["states"] is None:
            return []

        planes_list = []
        for state in raw_data["states"]:
            # Индексы согласно документации OpenSky:
            plane = Airplane(
                icao24=state[0], country=state[2], callsign=state[1], velocity=state[9], geo_altitude=state[7]
            )
            planes_list.append(plane)
        return planes_list


