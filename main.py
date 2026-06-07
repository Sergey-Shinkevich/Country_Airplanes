from src.airplanes import Airplane
from src.api import AirTrafficAPI
from src.file_operation import JSONSaver

if __name__ == "__main__":
    # 1. Получаем данные (api.airplanes уже содержит список объектов Airplane)
    api = AirTrafficAPI()
    api.get_data("Canada")

    # 2. Создаем объект-сохранитель
    saver = JSONSaver("data/data.json")

    # 3. Сохраняем полученные самолеты в файл
    saver.save_all(api.airplanes)
