from typing import Any, Generator, Iterator


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


# if __name__ == '__main__':
#     transactions = [
#         {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Payment"},
#         {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}, "description": "Transfer"},
#         {"id": 3, "operationAmount": {"amount": "150", "currency": {"code": "USD"}}, "description": "Refund"},
#     ]
#
#     usd_transactions = filter_by_currency(transactions, "USD")
#     print(usd_transactions)
#
#     # Использование filter_by_currency
#     for transaction in usd_transactions:
#         print(transaction)
#
#     # for _ in range(4):
#     #     try:
#     #         print(next(usd_transactions_1))
#     #     except StopIteration:
#     #         print("")
#
#     transactions = [
#         {
#             "id": 1,
#             "operationAmount": {"amount": "100.50", "currency": {"code": "USD"}},
#             "description": "Оплата товара",
#             "from": "Счет 12345678901234567890",
#             "to": "Счет 09876543210987654321",
#         },
#         {
#             "id": 2,
#             "operationAmount": {"amount": "200.00", "currency": {"code": "EUR"}},
#             "description": "Перевод другу",
#             "from": "Счет 11223344556677889900",
#             "to": "Счет 00998877665544332211",
#         },
#         {
#             "id": 3,
#             "operationAmount": {"amount": "150.75", "currency": {"code": "USD"}},
#             "description": "Возврат средств",
#             "from": "Счет 12345678901234567890",
#             "to": "Счет 00998877665544332211",
#         },
#     ]
#     description = transaction_descriptions(transactions)
#
#     # Использование transaction_descriptions
#     for transaction in description:
#         print(transaction)
#
#     # Использование  card_number_generator
#     for card_number in card_number_generator(1, 2):
#         print(card_number)
