import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тестирование файла src.masks функции get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1111222233334444", "1111 22** **** 4444"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("9999888877776666", "9999 88** **** 6666"),
])
def test_get_mask_card_number_multiple(card_number: str, expected: str) -> None:
    """Тест на кодирование номера с несколькими случаями"""
    assert get_mask_card_number(int(card_number)) == expected


@pytest.mark.parametrize("invalid_input, expected_exception", [
    ("11112222333344", ValueError),  # 14 цифр
    ("1", ValueError),  # 1 цифра
    ("111122223333444455", ValueError),  # 18 цифр
    ("", ValueError),
    (" ", ValueError),
    ("    ", ValueError),
    ("abcdefghijklmnop", ValueError),  # буквы
    ("1234abcd5678efgh", ValueError),  # цифры и буквы
    ("!@#$%^&*()_+{}|:", ValueError),  # символы
    ("1111-2222-3333-4444", ValueError),  # с дефисами
])
def test_get_mask_card_number_invalid(invalid_input: str, expected_exception: Exception) -> None:
    """Тест на ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(int(invalid_input))


# Тестирование файла src.masks функции get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("11111222225555588888", "**8888"),
])
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    """Тест на корректное кодирование валидных номеров счетов"""
    assert get_mask_account(int(account_number)) == expected


@pytest.mark.parametrize("invalid_account_number", [
    "736541084301358743",  # 18 цифр
    "1234567890",  # 10 цифр
    "1", #1 цифра
    "",  # пустая строка
    " ",  # пробел
    "     ",  # 5 пробелов
    "abcdefghijklmnop",  # буквы
    "1234abcd5678efgh",  # цифры и буквы
    "!@#$%^&*()_+{}|:"  # символы
])
def test_get_mask_account_invalid(invalid_account_number: str) -> None:
    """Тест на обработку невалидных номеров счетов"""
    with pytest.raises(ValueError):
        get_mask_account(int(invalid_account_number))
