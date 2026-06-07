import json
import os
from abc import ABC, abstractmethod
from typing import Any

from src.airplanes import Airplane


class AbstractSaver(ABC):
    """Абстрактный класс-коннектор"""

    @abstractmethod
    def add_airplane(self, airplane: Airplane) -> None:
        """Шаблон метода добавления нового самолета"""
        pass

    @abstractmethod
    def get_all(self, **kwargs: Any) -> list[Airplane]:
        """Шаблон метода чтения всего файла"""
        pass

    @abstractmethod
    def delete_airplane(self, icao24: str) -> None:
        """Шаблон метода удаления самолета по icao24"""
        pass


class JSONSaver(AbstractSaver):
    """Реализация класса с типом данных JSON"""

    def __init__(self, filename: str):
        """Конструктор класса"""
        self.filename = filename

    def add_airplane(self, airplane: Airplane) -> None:
        """Добавление самолета"""
        airplanes_list = self.get_all()
        if any(p.icao24 == airplane.icao24 for p in airplanes_list):
            print(f"Самолет {airplane.icao24} уже есть в базе!")
            return
        airplanes_list.append(airplane)

        data_to_save = [vars(p) for p in airplanes_list]

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        print(f"Самолет {airplane.callsign} (ICAO24: {airplane.icao24}) добавлен в {self.filename}")

    def get_all(self, **kwargs: Any) -> list[Airplane]:
        """Считывает данные и превращает их в список объектов Airplane"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return [Airplane.from_dict(item) for item in data]
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Ошибка при чтении файла: {e}")
                return []

    def delete_airplane(self, icao24: str) -> None:
        """Удаление самолета по icao24"""
        airplanes_list = self.get_all()
        new_list = [p for p in airplanes_list if p.icao24 != icao24]

        if len(new_list) < len(airplanes_list):
            data_to_save = [vars(p) for p in new_list]
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
            print(f"Самолет с ICAO24 {icao24} успешно удален.")
        else:
            print(f"Внимание: самолет с ICAO24 {icao24} не найден в файле.")

    def save_all(self, airplanes_list: list[Airplane]) -> None:
        """Полная перезапись файла актуальными данными"""
        data_to_save = [vars(p) for p in airplanes_list]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        print(f"База обновлена. Теперь в ней {len(airplanes_list)} самолетов.")
