import json


def get_transaction(file):
    """Принимает файл JSON и возвращает список словарей"""
    try:
        with open(file, "r", encoding='utf-8') as transaction:
            if not transaction:
                return []
            try:
                transaction = json.load(transaction)
                return transaction
            except json.JSONDecodeError:
                print("Ошибка файла")
            except Exception:
                print("Что-то не так...(С файлом или содержимым")
                return []
    except FileNotFoundError:
        print("Файл не найден")
    return False

    sum_transactions = sum(transaction[amount].value())
    print(sum_transactions)

# def sum_transactions(transaction):









if __name__ == "__main__":
    get_transaction(file="D:\\PythonProject\\PythonProject_NPR\\data/operations.json")
