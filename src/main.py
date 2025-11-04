from typing import Any

from src.financial_operations import read_csv_transactions, read_excel_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction


def main():
    data = file_format("D:/PythonProject/PythonProject_NPR/transactions.csv",
                       "D:/PythonProject/PythonProject_NPR/transactions_excel.xlsx",
                       "D:/PythonProject/PythonProject_NPR/data/operations.json")
    file_format_result = search_operation_status(data)
    search_operation_status_result = sorting_data_operations(file_format_result)
    sorting_by_nominal = nominal(search_operation_status_result)


def file_format(filename_csv=None, filename_excel=None, file_json=None):
    """
    Запрос от пользователя из какого формата получить транзакцию
    :param file_json:
    :param filename_csv:
    :param filename_excel:
    :return:
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    # Получение информации в форматах JSON, CSV или XLSX
    while True:
        search_file = input("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""").strip().lower()
        if search_file == "1":
            print(f"Для обработки выбран JSON-файл")
            result_format = get_transaction(file_json)
            return result_format
        elif search_file == "2":
            print(f"Для обработки выбран CSV-файл")
            result_format = read_csv_transactions(filename_csv)
            return result_format
        elif search_file == "3":
            print(f"Для обработки выбран XLSX-файл")
            result_format = read_excel_transactions(filename_excel)
            return result_format
        else:
            print(f"Введено неверное значение {search_file}")
            continue

def search_operation_status(data: list[dict]) -> list[dict]:
    """
    Фильтрация операций по статусу "STATE"
    :param data: Из какого формата брать информацию
    :return: Выборку по EXECUTED, CANCELED или PENDING
    """
    if data is None:
        print("Получены пустые данные")
        return []
    while True:
        operation_status = input(
            f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().lower()

        if operation_status in ["executed", "canceled", "pending"]:
            result_status_operations = filter_by_state(data, operation_status)
            return result_status_operations
        else:
            print(f"Статус операции {operation_status} недоступен")
            continue

def sorting_data_operations(file):
    """
    Сортировка данных по дате операции
    :param file: получение данных из def search_operation_status
    :return: отсортированные данный по дате
    """
    while True:
        sorting_data_input = input("Отсортировать операции по дате? Да/Нет\n").lower().strip()
        if sorting_data_input in ["да"]:
            sort_ascending_descending = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if sort_ascending_descending in ["по возрастанию", "по убыванию"]:
                if sort_ascending_descending == "по возрастанию":
                    file = sort_by_date(file, reverse=False)
                    return file
                elif sort_ascending_descending == "по убыванию":
                    file = sort_by_date(file, reverse=True)
                    return file
            else:
                file = sort_by_date(file, reverse=False)
                print("Неправильно выбрана команда, сортируется по убыванию")
                return file
        elif sorting_data_input in ["нет"]:
            print(f"Не сортируется по дате{file}")
            return file
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")
            continue


    # Сортировка по номиналу

def nominal(search_operation, currency=None):
    """
    Сортировка по номиналу из def sorting_data_operations(file)
    :param search_operation: Список словарей
    :param currency: Сортировать по RUB
    :return:
    """
    print(search_operation)
    while True:
        sorting_value = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if sorting_value in ["да"]:
            currency = "RUB"
            sorted_nominal = filter_by_currency(search_operation, currency)
            sorted_nominal_list = list(sorted_nominal)
            if not sorted_nominal_list:
                print("Рублевых транзакций не найдено")
                return search_operation
            return sorted_nominal_list
        elif sorting_value in ["нет"]:
            return search_operation
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")
            continue


    # Сортировка по ключевому слову
def keyword():
    while True:
        sorting_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if sorting_by_word in ["да"]:
            keyword = input("Введите слово для поиска в описании: ").strip()
            pass  # Функция сортировки по слову
        print("Не сортируется по ключевому слову")

    print("Распечатываю итоговый список транзакций...")
    pass

if __name__ == "__main__":
    start = main()
    # file_format("D:/PythonProject/PythonProject_NPR/transactions.csv",
    #             "D:/PythonProject/PythonProject_NPR/transactions_excel.xlsx",
    #             "D:/PythonProject/PythonProject_NPR/data/operations.json")
