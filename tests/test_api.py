from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.api import AirTrafficAPI


def test_initialization() -> None:
    """Проверка, что класс создается корректно"""
    api = AirTrafficAPI()
    assert api.airplanes == []


@patch("src.api.AirTrafficAPI.connect")  # Мокаем connect
def test_invalid_country(mock_connect: Any) -> None:
    """Проверка обработки несуществующей страны"""
    mock_connect.return_value = True
    api = AirTrafficAPI()

    with patch("src.api.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = []
        mock_get.return_value = mock_resp
        with pytest.raises(ValueError, match="не найдена"):
            api.get_data("NonExistentCountryName123")


@patch("src.api.AirTrafficAPI.connect")
@patch("src.api.requests.get")
@patch("src.airplanes.Airplane.from_api")  # Мокаем фабрику
def test_get_data_success(mock_from_api: Any, mock_get: Any, mock_connect: Any) -> None:
    """Тестируем успешный сценарий"""
    mock_connect.return_value = True

    mock_resp_geo = MagicMock()
    mock_resp_geo.json.return_value = [{"boundingbox": ["1", "2", "3", "4"]}]

    mock_resp_sky = MagicMock()
    mock_resp_sky.json.return_value = {"states": [["data_for_airplane"]]}

    mock_get.side_effect = [mock_resp_geo, mock_resp_sky]

    mock_plane = MagicMock()
    mock_plane.icao24 = "icao1"
    mock_from_api.return_value = mock_plane

    api = AirTrafficAPI()
    api.get_data("Canada")

    assert len(api.airplanes) == 1
    assert api.airplanes[0].icao24 == "icao1"
    mock_from_api.assert_called_once()
