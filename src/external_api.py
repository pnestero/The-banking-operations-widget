import json
import os
from typing import Tuple

import requests
from dotenv import load_dotenv

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def transactions_sum(file: str) -> Tuple[float, float, float]:
    """Принимает транзакции и возвращает их по валюте"""
    with open(file, "r", encoding="utf-8") as f:
        transactions_list = json.load(f)
    total_sum_rub = 0.0
    total_sum_usd = 0.0
    total_sum_eur = 0.0

    for transaction in transactions_list:
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                total_sum_rub += round((float(transaction["operationAmount"]["amount"])), 2)
            elif transaction["operationAmount"]["currency"]["code"] == "USD":
                total_sum_usd += round((float(transaction["operationAmount"]["amount"])), 2)
            elif transaction["operationAmount"]["currency"]["code"] == "EUR":
                total_sum_eur += round((float(transaction["operationAmount"]["amount"])), 2)

    print(round(total_sum_rub, 2), round(total_sum_usd, 2), round(total_sum_eur, 2))
    return total_sum_rub, total_sum_usd, total_sum_eur


def currency_conversion(total_sum_rub, total_sum_usd, total_sum_eur, rate_usd=None):
    """Конвертирование валюты в рубли"""
    headers = {"apikey": API_KEY}

    result_usd = 0.0
    result_eur = 0.0

    # Конвертируем EUR в RUB

    try:
        if total_sum_eur > 0:
            rate_eur = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={total_sum_eur}",
                headers=headers,
                timeout=20,
            )
            print(f"Cтатус передачи данных {rate_usd.status_code}")
            if rate_eur.status_code == 200:
                data_eur = rate_eur.json()
                if "result" in data_eur:
                    result_eur = data_eur["result"]
                    print("EUR конвертация успешна: {result_eur}")
                else:
                    result_eur = total_sum_eur * 90
                    print("Ошибка в получении ключа result от сайта")
            else:
                result_eur = total_sum_eur * 90.0
                print("Ошибка в запросе на сайт")
        else:
            result_eur = 0.0
            print("EUR = 0, конвертация не требуется")

        # Конвертируем USD в RUB

        if total_sum_usd > 0:
            rate_usd = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={total_sum_usd}",
                headers=headers,
                timeout=20,
            )
            print(f"Cтатус передачи данных {rate_usd.status_code}")
            if rate_usd.status_code == 200:
                data_usd = rate_usd.json()
                if "result" in data_usd:
                    result_usd = data_usd["result"]
                    print(f"USD конвертация успешна: {result_usd}")
                else:
                    result_usd = total_sum_usd * 90
                    print("Ошибка в получении ключа 'result' от сайта")
            else:
                result_usd = total_sum_usd * 90.0
                print("Ошибка в запросе на сайт")
        else:
            result_usd = 0.0
            print("USD сумма = 0, конвертация не требуется")
    except requests.exceptions.Timeout:
        print("Превышено время ожидания ответа от сервера")
    except requests.exceptions.ConnectionError:
        print("Нет соединения с интернетом или сервер недоступен")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сетевого запроса: {e}")
    except json.JSONDecodeError:
        print("Не удалось разобрать ответ сервера (неверный JSON)")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")

    # Итого сумма
    result_sum = total_sum_rub + result_usd + result_eur
    return result_sum


if __name__ == "__main__":
    total_sum_rub, total_sum_usd, total_sum_eur = transactions_sum(
        file="D:\\PythonProject\\PythonProject_NPR\\data/operations.json"
    )
    result = currency_conversion(total_sum_rub, total_sum_usd, total_sum_eur)
    print(result)
