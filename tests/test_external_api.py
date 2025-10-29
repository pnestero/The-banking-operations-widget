import json
from unittest.mock import Mock, mock_open, patch

from src.external_api import transactions_sum, currency_conversion
from src.utils import get_transaction


def test_currency_conversion(transactions: dict) -> None:
    """Тест на конвертацию валют"""
    with patch("builtins.open", mock_open(read_data=json.dumps(transactions))):
        with patch("requests.get") as mock_requests:
            with patch("os.path.exists") as mock_path_exists:
                mock_path_exists.return_value = True
                mock_requests.return_value.status_code = 200
                mock_requests.return_value.json.return_value = {"result": 0}
                assert transactions_sum(" ") == 100

def test_currency_conversion_status_code():
    """Проверка status_code != 200"""
    assert currency_conversion({}) == 0



@patch("builtins.open", side_effect=json.JSONDecodeError("123", "321", 1))
def test_decode_error(mock_open: Mock) -> None:
    """Тест на выброс ошибки при пустом словаре"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []


@patch("builtins.open", side_effect=Exception)
def test_decode_error_exception(mock_file: Mock) -> None:
    """Тест, если файл битый"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []
