from typing import Any


class Airplane:
    def __init__(self, icao24: str, country: str, callsign: Any, velocity: float, geo_altitude: float):
        """Конструктор класса Airplanes"""
        self.icao24 = icao24
        self.country = country
        self.callsign = (icao24[0:3] + country) if callsign is None else callsign
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
