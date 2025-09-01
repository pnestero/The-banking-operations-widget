import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тестирование файла src.masks функции get_mask_card_number
@pytest.mark.parametrize()
def test_get_mask_card_number():
    """Тест на кодирование номера"""
    assert get_mask_card_number("1111222233334444") == "1111 22** **** 4444"


def test_get_mask_card_number_len():
    """Тест на неправильную длину номера карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("11112222333344")


def test_get_mask_card_number_string_without_data():
    """Тест на передачу пустого значения"""
    with pytest.raises(ValueError):
        get_mask_card_number("")
        get_mask_card_number(" ")


def test_get_mmt_digit_input():
    """Тест нечислового ввода"""
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")  # буквы вместо цифр
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd5678efgh")  # смесь цифр и букв


# Тестирование файла src.masks функции get_mask_account
def test_get_mask_account():
    """Тест на кодирование номера"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_len():
    """Тест на неправильную длину номера аккаунта"""
    with pytest.raises(ValueError):
        get_mask_account("736541084301358743")


def test_get_mask_account_string_without_data():
    """Тест на передачу пустого значения"""
    with pytest.raises(ValueError):
        get_mask_account("")
        get_mask_account(" ")


def test_get_mask_account_input():
    """Тест нечислового ввода"""
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmnop")  # буквы вместо цифр
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd5678efgh")  # смесь цифр и букв
