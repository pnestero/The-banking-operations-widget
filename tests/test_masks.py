import pytest

from src.masks import get_mask_card_number


# Тестирование файла src.masks функции get_mask_card_number
def test_mask_card_number():
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert get_mask_card_number("1111222233334444") == "1111 22** **** 4444"


def test_mask_card_number_len():
    with pytest.raises(ValueError):
        get_mask_card_number("123412341234134")
        get_mask_card_number("12345678901234567")


def test_mask_card_number_string_without_data():
    with pytest.raises(ValueError):
        get_mask_card_number("")
        get_mask_card_number(" ")


def test_mmt_digit_input():
    """Тест нечислового ввода"""
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("abcdefghijklmnop")  # буквы вместо цифр

    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры"):
        get_mask_card_number("1234abcd5678efgh")  # смесь цифр и букв