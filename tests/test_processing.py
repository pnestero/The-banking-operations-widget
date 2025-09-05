from typing import Dict, Any

import pytest

from src.processing import filter_by_state, sort_by_date


# Параметризация для файла processing.py функции filter_by_state
@pytest.mark.parametrize(
    "transactions, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_filter_by_state(transactions: list[dict], state: str, expected: list[dict]) -> None:
    """Тест фильтрации"""
    assert filter_by_state(transactions, state) == expected


@pytest.fixture
def mixed_state_data() -> list[Dict[str, Any]]:
    """Фикстура со смешанными состояниями операций"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-15T12:30:45.123456", "amount": 100.50},
        {"id": 2, "state": "CANCELED", "date": "2023-10-14T15:45:22.789012", "amount": 250.75},
        {"id": 3, "state": "PENDING", "date": "2023-10-13T09:12:33.456789", "amount": 500.00},
        {"id": 4, "state": "EXECUTED", "date": "2023-10-12T18:20:15.321654", "amount": 75.25},
        {"id": 5, "state": "FAILED", "date": "2023-10-11T14:05:10.987654", "amount": 300.00},
        {"id": 6, "state": "EXECUTED", "date": "2023-10-10T11:30:05.654321", "amount": 150.00},
        {"id": 7, "state": "CANCELED", "date": "2023-10-09T16:40:30.123789", "amount": 425.50},
        {"id": 8, "state": "EXECUTED", "date": "2023-10-08T13:15:20.456123", "amount": 200.00},
    ]


def test_filter_by_state_list(list_operation: list[dict]) -> None:
    """Тест фильтра по значению "EXECUTED" """
    assert (
        filter_by_state(
            [
                {"id": 1, "state": "EXECUTED", "date": "2023-10-15T12:30:45.123456", "amount": 100.50},
                {"id": 2, "state": "CANCELED", "date": "2023-10-14T15:45:22.789012", "amount": 250.75},
                {"id": 3, "state": "PENDING", "date": "2023-10-13T09:12:33.456789", "amount": 500.00},
                {"id": 4, "state": "EXECUTED", "date": "2023-10-12T18:20:15.321654", "amount": 75.25},
                {"id": 5, "state": "FAILED", "date": "2023-10-11T14:05:10.987654", "amount": 300.00},
                {"id": 6, "state": "EXECUTED", "date": "2023-10-10T11:30:05.654321", "amount": 150.00},
                {"id": 7, "state": "CANCELED", "date": "2023-10-09T16:40:30.123789", "amount": 425.50},
                {"id": 8, "state": "EXECUTED", "date": "2023-10-08T13:15:20.456123", "amount": 200.00},
            ]
        )
        == list_operation
    )


def test_sort_data_operation(sort_data_operation: Any) -> None:
    """Тест сортировки даты"""
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == sort_data_operation
    )
