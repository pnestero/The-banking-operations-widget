from typing import Dict, Any

import pytest


# ФИКСТУРЫ для файла masks.py

# Фикстура для test_get_mask_account_valid в masks.py
@pytest.fixture
def card_number() -> list[tuple[str, str]]:
    return [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]


# Фикстура для test_get_mask_account_valid_fixture в masks.py
@pytest.fixture
def mask_account() -> list[tuple[str, str]]:
    return [("73654108430135874305", "**4305"),
            ("12345678901234567890", "**7890"),
            ("11111222225555588888", "**8888")]


@pytest.fixture
def mask_card_number() -> list[tuple[str, str]]:
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ]


@pytest.fixture
def account_number() -> list[tuple[str, str]]:
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("11111222225555588888", "**8888")
    ]


# Тесты для processing.py функции def filter_by_state

@pytest.fixture
def executed_state_data() -> list[Dict[str, Any]]:
    """Фикстура только с EXECUTED операциями"""
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def same_date_data() -> list[Dict[str, Any]]:
    """Фикстура с одинаковыми датами"""
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
