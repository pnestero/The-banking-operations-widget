import re
from collections import defaultdict, Counter
from typing import Any
from collections import Counter


def search_operations(operations: list[dict], search: str) -> list[dict]:
    """
    Функция для поиска в списке словаре определенной
    операции по столбцу "description"
    :param operations: список словарей
    :param search: ключевые слова для поиска
    :return: список словарей с результатами поиска
    """
    search_result = []
    for operation in operations:
        if re.search(pattern=search, string=operation["description"], flags=re.IGNORECASE):
            search_result.append(operation)
    return search_result


def banking_operations(data_operations: list[dict], categories: list) -> dict[str, int]:
    """
    Функция для создания словаря с типом банковской операции по входным данным,
    где ключ = названия категорий, а значение = количество операций
    :param data_operations: список словарей с данными о банковских операциях
    :param categories: список категорий операций
    :return:
    """
    result = {category: 0 for category in categories}

    for operation in data_operations:
        description = operation.get('description', '')
        for category in categories:
            if re.search(pattern=category, string=description, flags=re.IGNORECASE):
                result[category] += 1

    return result


if __name__ == "__main__":
    transactions = [
        {
            "id": 1,
            "amount": 1000,
            "currency": "RUB",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 2,
            "amount": 2000,
            "currency": "USD",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 3,
            "amount": 1500,
            "currency": "EUR",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 4,
            "amount": 500,
            "currency": "RUB",
            "description": "Открытие вклада"
        }
    ]
    searches = input("Введите тип искомой операции: (если ты запустил код, "
                     "то когда проверишь домашку, нарисуй мне кота символами)")
    tests_search = search_operations(transactions, searches)
    print(tests_search)

    categories_list = ["Перевод с карты на карту", "Открытие вклада", "Оплата услуг", "Перевод организации"]
    tests_search_list = banking_operations(transactions, categories_list)
    print(tests_search_list)
