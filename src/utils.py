import json, os
from typing import Any


def get_transaction(file: str) -> list[Any] | bool | Any:
    """Принимает файл JSON и возвращает список словарей"""
    file_exist = os.path.exists(file)
    if not file_exist:
        return []
    try:
        with open(file, "r", encoding="utf-8") as transaction:
            transaction = json.load(transaction)
            if not isinstance(transaction, list):
                return []
            return transaction
    except json.JSONDecodeError:
        print("Ошибка файла")
        return []
    except Exception:
        print("Что-то не так...(С файлом или содержимым")
        return []


if __name__ == "__main__":
    result = get_transaction(file="D:\\PythonProject\\PythonProject_NPR\\data/operations.json")
    print(result)
