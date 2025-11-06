import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("D:/PythonProject/PythonProject_NPR/logs/utils.log", "w", "utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction(file: str) -> list[Any] | bool | Any:
    """Принимает файл JSON и возвращает список словарей"""
    file_exist = os.path.exists(file)
    if not file_exist:
        logger.error(f"Файл {file} не найден")
        return []
    try:
        with open(file, "r", encoding="utf-8") as transaction:
            transaction = json.load(transaction)
            if not isinstance(transaction, list):
                logger.error(f"Файл {file} не является списком")
                return []
            logger.info(f"Файл {file} открылся и информация записана")
            return transaction
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования в {file}, ошибка: {e}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка {e} при работе с файлом {file}")
        return []
