from abc import ABC, abstractmethod
from typing import Any, Dict, Union

import requests


class APIClient(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_data(self, *args: Any, **kwargs: Any) -> Any:
        """Шаблон метода получения данных с API"""
        pass


# 2. Тот самый класс, который просят в задании
class AirTrafficAPI(APIClient):
    """Класс получения самолетов на данной территории"""

    def __init__(self) -> None:
        """Метод - конструктор"""
        self.__nominatim_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all"
        self.aeroplanes = None

    def get_data(self, country: str) -> None:
        """Метод получения самолетов на данной территории"""
        try:
            # Работа с openstreetmap
            headers = {"User-Agent": "test-app"}
            params_nominatim: Dict[str, Any] = {'country': country, 'format': 'json', 'limit': 1}
            response_geo = requests.get(self.__nominatim_url, params=params_nominatim, headers=headers, timeout=10)
            response_geo.raise_for_status()
            geo_data = response_geo.json()
            if not isinstance(geo_data, list) or not geo_data:
                raise ValueError(f"Страна {country} не найдена.")
            item = geo_data[0]
            bbox = item.get('boundingbox')
            if not bbox:
                raise ValueError(f"Координаты для {country} не найдены.")

            # Работа с opensky-network
            params_sky: Dict[str, Any] = {"lamin": bbox[0], "lamax": bbox[1], "lomin": bbox[2], "lomax": bbox[3]}
            response_sky = requests.get(self.__opensky_url, params=params_sky, timeout=10)
            response_sky.raise_for_status()
            self.aeroplanes = response_sky.json()

            # Обработка ошибок
        except ValueError:
            raise
        except requests.exceptions.RequestException as e:
            print(f"Сетевая ошибка: {e}")


# Использование
api = AirTrafficAPI()
api.get_data("Canada")
print(api.aeroplanes)
