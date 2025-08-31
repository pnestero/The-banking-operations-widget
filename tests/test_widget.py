import pytest

from src.widget import mask_card_number, get_date


# Тестирование файла src.masks функции mask_card_number
# Параметризация для def mask_card_number
@pytest.mark.parametrize("input_card", "output_card", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 64686473678894779589", "Счет **9589")
])
def test_mask_card_number(input_card, output_card):
    """Тест входных данных карт и счетов"""
    assert mask_card_number(input_card) == output_card


def test_mask_card_number():
    """Тест на кодирование номера"""
    assert mask_card_number("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_card_number("Счет 64686473678894779589") == "Счет **9589"


def test_mask_card_number_len():
    """Тест на неправильную длину номера карты"""
    with pytest.raises(ValueError):
        mask_card_number("Visa Platinum 70007922896361")
        mask_card_number("Счет 646864736788979589")


def test_mask_card_number_string_without_data():
    """Тест на передачу пустого значения"""
    with pytest.raises(ValueError):
        mask_card_number("")
        mask_card_number(" ")


def test_mask_card_number_input():
    """Тест нечислового ввода"""
    with pytest.raises(ValueError):
        mask_card_number("Visa Platinum hjdlghwtpbcdfgju")  # буквы вместо цифр
    with pytest.raises(ValueError):
        mask_card_number("Счет sss8647367889477958s")  # смесь цифр и букв


# Тест src/widget.py функции def get_date
# Параметризация для def get_date
@pytest.mark.parametrize("input_date, out_data",
                         [
                             ("2024-03-11T02:26:18.671407", "11.03.2024"),
                             ("2024-03-11T02:26:18", "11.03.2024"),
                             ("2024-03-11T00:00:00", "11.03.2024"),
                             ("2024-03-11T23:59:59.999999", "11.03.2024"),
                             ("0001-01-01T00:00:00", "01.01.0001"),
                             ("9999-12-31T23:59:59", "31.12.9999"),
                             ("2024-03-11T02:26:18.123", "11.03.2024"),
                             ("2024-03-11T02:26:18.1", "11.03.2024")
                         ])
def test_date_formats(input_date, out_data):
    """Тест различных форматов даты и времени"""
    assert get_date(input_date) == out_data


def test_basic_date_conversion():
    """Тест базового преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_strings_without_date():
    """Тест строк, где отсутствует дата"""
    no_date_strings = [
        "",  # Пустая строка
        "   ",  # Пробелы
        "12:26:18",  # Только время
    ]
    for no_date_string in no_date_strings:
        with pytest.raises(ValueError):
            get_date(no_date_string)
