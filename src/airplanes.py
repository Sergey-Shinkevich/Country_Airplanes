from typing import Any


class Airplane:
    def __init__(self, icao24: Any, country: Any, callsign: Any, velocity: Any, geo_altitude: Any):
        """Конструктор класса Airplanes"""
        self.icao24 = icao24
        self.country = country

        if callsign is None or str(callsign).strip() == "":
            self.callsign = str(icao24)[0:3] + str(country)
        else:
            self.callsign = callsign

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

    @classmethod
    def from_api(cls, state: list) -> Any:
        """Проверки для данных из API"""
        if not state or len(state) < 10:
            return None
        return cls(icao24=state[0], country=state[2], callsign=state[1], velocity=state[9], geo_altitude=state[7])

    @classmethod
    def from_dict(cls, data: dict) -> Any:
        """Логика для чтения из файла"""
        return cls(data["icao24"], data["country"], data["callsign"], data["velocity"], data["geo_altitude"])
