import csv
from typing import Any

import pandas as pd


def read_csv_transactions(filename_csv: str) -> list[Any] | str:
    """
    Считывание CSV файли и возвращает список словарей,
    :param filename_csv: передаётся файл CSV
    :return: список словарей
    """
    transactions_csv_return = []
    try:
        with open(filename_csv, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                transactions_csv_return.append(row)
        return transactions_csv_return
    except FileNotFoundError:
        return "Файл CSV не обнаружен или неверный формат файла"


def read_excel_transactions(filename_excel: str) -> list[Any] | str:
    """
    Считывание Excel файли и возвращает список словарей,
    :param filename_excel: Excel файл
    :return: список словарей операций из файла Excel
    """
    try:
        reader = pd.read_excel(filename_excel)
        return reader.to_dict("records")
    except FileNotFoundError:
        return "Файл Excel не обнаружен или неверный формат файла"
