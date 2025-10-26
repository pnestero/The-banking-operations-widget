import csv
import pprint

import pandas as pd


def read_csv_transactions(filename_csv: str) -> list:
    """
    Считывание CSV файли и возвращает список словарей,
    :param filename_csv: передаётся файл CSV
    :return: список словарей
    """
    transactions_csv_return = []
    with open(filename_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            transactions_csv_return.append(row)
    return transactions_csv_return


def read_excel_transactions(filename_excel: str) -> list:
    """
    Считывание Excel файли и возвращает список словарей,
    :param filename_excel: Excel файл
    :return: список словарей операций из файла Excel
    """
    transactions_excel_return = []

    reader = pd.read_excel(filename_excel)
    for index, row in reader.iterrows():
        transactions_excel_return.append(row.to_dict())
    return transactions_excel_return


if __name__ == "__main__":
    transactions_csv = read_csv_transactions("../transactions.csv")
    pprint.pprint(transactions_csv, width=120, depth=7)
    print("Чтение CSV окончено")

    transactions_excel = read_excel_transactions("../transactions_excel.xlsx")
    pprint.pprint(transactions_excel, width=120, depth=7)
    print("Чтение Excel окончено")
