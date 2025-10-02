import json
from typing import Any


def get_transaction(file: str) -> list[Any] | bool | Any:
    """Принимает файл JSON и возвращает список словарей"""
    try:
        with open(file, "r", encoding="utf-8") as transaction:
            if not transaction:
                return []
            try:
                transaction = json.load(transaction)
                return transaction
            except json.JSONDecodeError:
                print("Ошибка файла")
                return []
            except Exception:
                print("Что-то не так...(С файлом или содержимым")
                return []
    except FileNotFoundError:
        print("Файл не найден")
    return False


if __name__ == "__main__":
    result = get_transaction(file="D:\\PythonProject\\PythonProject_NPR\\data/operations.json")
    print(result)
