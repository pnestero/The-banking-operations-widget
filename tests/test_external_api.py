import json
from unittest.mock import Mock, mock_open, patch

from more_itertools.more import side_effect

from src.external_api import currency_conversion, transactions_sum
from src.utils import get_transaction


def test_currency_conversion(transactions):
    """<UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK>"""
    with patch("builtins.open", mock_open(read_data=json.dumps(transactions))) as mock_file:
        with patch("requests.get") as mock_requests:
            with patch("os.path.exists") as mock_path_exists:
                mock_path_exists.return_value = True
                mock_requests.return_value.status_code = 200
                mock_requests.return_value.json.return_value = {"result": 0}
                assert transactions_sum(" ") == 100


@patch("builtins.open", side_effect=json.JSONDecodeError("123", "321", 1))
def test_decode_error(mock_open):
    """Тест на выброс ошибки при пустом словаре"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []



@patch("builtins.open", side_effect=Exception)
def test_decode_error_exception(mock_file):
    """Тест, если файл битый"""
    assert get_transaction(" ") == []
    with patch("os.path.exists") as mock_path_exists:
        mock_path_exists.return_value = True
        assert get_transaction(" ") == []
