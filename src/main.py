from src.financial_operations import read_csv_transactions, read_excel_transactions
from src.utils import get_transaction


def main():
    pass


def file_format(filename_csv=None, filename_excel=None, file=None):
    """
    Запрос от пользователя
    :param filename_csv:
    :param filename_excel:
    :param file:
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
            json_format = get_transaction(file)
            break
        elif search_file == "2":
            print(f"Для обработки выбран CSV-файл")
            csv_format = read_csv_transactions(filename_csv)
            break
        elif search_file == "3":
            print(f"Для обработки выбран XLSX-файл")
            json_format = read_excel_transactions(filename_excel)
            break
        else:
            print(f"Введено неверное значение {search_file}")
            continue

    # Статус банковской операции
    while True:
        search_operation_status = input(
            f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().lower()

        if search_operation_status in ["executed", "canceled", "pending"]:
            if search_operation_status == "executed":
                print('Операции отфильтрованы по статусу EXECUTED\n')
                break
            elif search_operation_status == "canceled":
                print('Операции отфильтрованы по статусу CANCELED\n')
                break
            elif search_operation_status == "pending":
                print('Операции отфильтрованы по статусу PENDING\n')
                break
        else:
            print(f"Статус операции {search_operation_status} недоступен")
            continue

    # Сортировка операции по дате да/нет
    while True:
        sorting_data = input("Отсортировать операции по дате? Да/Нет\n").lower().strip()
        if sorting_data in ["да"]:
            print("Сортируется по дате")
            break # функция по сортировке по дате
        elif sorting_data in ["нет"]:
            print("Не сортируется по дате")
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")
            continue

    # Сортировка по возрастанию или по убыванию?
    while True:
        sort_ascending_descending = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if sort_ascending_descending in ["по возрастанию", "по убыванию"]:
            if sort_ascending_descending == "по возрастанию":
                break   # Функция по возрастанию
            elif sort_ascending_descending == "по убыванию":
                break   # Функция по убыванию
        else:
            # Функция по убыванию
            print("Неправильно выбрана команда, сортируется по убыванию")

    # Сортировка по номиналу
    while True:
        sorting_value = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if sorting_value in ["да"]:
            break  # Функция сортировки по валюте
        else:
            print("Не сортируется по валюте")

    # Сортировка по ключевому слову
    while True:
        sorting_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if sorting_by_word in ["да"]:
            keyword = input("Введите слово для поиска в описании: ").strip()
            break  # Функция сортировки по слову
        print("Не сортируется по ключевому слову")

    print("Распечатываю итоговый список транзакций...")


if __name__ == "__main__":
    file_format("D:/PythonProject/PythonProject_NPR/transactions.csv",
                "D:/PythonProject/PythonProject_NPR/transactions_excel.xlsx",
                )
