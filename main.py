from src.airplanes import Airplane
from src.api import AirTrafficAPI
from src.file_operation import JSONSaver
from src.utils import filter_airplanes, get_top_airplanes, print_airplanes, sort_airplanes


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    # 1. Пользовательский ввод данных
    country = input("Введите название страны: ")
    top_n = int(input("Введите количество самолетов для вывода в топ N по высоте полета: "))
    filter_country = input("Введите название страны для фильтрации по стране регистрации: ")

    # 2. Получение данных
    api = AirTrafficAPI()
    api.get_data(country)

    # 3. Сохранение
    saver = JSONSaver("data/data.json")
    saver.save_all(api.airplanes)

    # 4. Добавление самолета и его записи
    airplane = Airplane("UAL1621", "United States", "Letun", 268.79, 10203.18)
    saver.add_airplane(airplane)

    # 5. Удаление добавленного самолета.
    saver.delete_airplane("UAL1621")

    # 6. Чтение из файла
    all_data = saver.get_all()

    # 7. Фильтр по стране регистрации
    filtered_airplanes = filter_airplanes(all_data, filter_country)

    # 8. Сортировка по высоте полета отфильтрованных данных
    sorted_airplanes = sort_airplanes(filtered_airplanes)

    # 9. Вывод Топ N самолетов
    top_airplanes = get_top_airplanes(sorted_airplanes, top_n)
    print_airplanes(top_airplanes)


if __name__ == "__main__":
    user_interaction()
