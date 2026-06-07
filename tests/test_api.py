from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.api import AirTrafficAPI


def test_initialization() -> None:
    """Проверка, что класс создается корректно"""
    api = AirTrafficAPI()
    assert api.airplanes is None


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


@patch("src.api.AirTrafficAPI.connect")  # Мокаем connect
@patch("src.api.requests.get")  # Мокаем requests.get
def test_get_data_success(mock_get: Any, mock_connect: Any) -> None:
    """Тестируем успешный сценарий с замоканным коннектом"""
    mock_connect.return_value = True

    mock_resp_geo = MagicMock()
    mock_resp_geo.status_code = 200
    mock_resp_geo.json.return_value = [{"boundingbox": ["1", "2", "3", "4"]}]

    mock_resp_sky = MagicMock()
    mock_resp_sky.status_code = 200
    mock_resp_sky.json.return_value = {"states": [["icao1", "callsign1"]]}
    mock_get.side_effect = [mock_resp_geo, mock_resp_sky]

    api = AirTrafficAPI()
    api.get_data("Canada")

    assert api.airplanes is not None
    assert api.airplanes["states"][0][0] == "icao1"
    assert mock_get.call_count == 2
    mock_connect.assert_called_once()
