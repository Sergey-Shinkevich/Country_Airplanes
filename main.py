from src.airplanes import Airplane
from src.api import AirTrafficAPI

if __name__ == "__main__":
    # 1. Создание экземпляра класса для работы с API сайтов с самолетами
    api = AirTrafficAPI()

    # 2. Получение информации о самолетах с opensky-network.org
    api.get_data("Canada")
    airplanes = api.airplanes

    # 3. Преобразование набора данных в список объектов
    airplanes = Airplane.cast_to_object_list(airplanes)


