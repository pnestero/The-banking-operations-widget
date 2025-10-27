from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Принимает на вход список словарей с транзакциями.
    Возвращает итератор, где валюта операции соответствует искомой.
    :param transactions: Принимает на вход список словарей
    :param currency: принимает в себя искомое значение
    :return: возвращает словарь
    """
    filter_transactions = filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("code") == currency, transactions
    )
    return filter_transactions


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> list:
    """Генерирует номер карты в заданном диапазоне"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Некорректный номер")
    if start < 1 or stop > 9999999999999999 or start > stop:
        raise ValueError("Неправильные вводимые данные")
    numb_card = []
    for number in range(start, stop + 1):
        # Форматируем число как строку с ведущими нулями и разбиваем на группы по 4 цифры
        format_number = str("{:16d}".format(number)).replace(" ", "0")
        card_number = f"{format_number[:4]} {format_number[4:8]} {format_number[8:12]} {format_number[12:]}"
        numb_card.append(card_number)
    return numb_card
