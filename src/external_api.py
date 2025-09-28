import json, requests
from typing import Any


def transactions_sum(file: str) -> tuple[float | Any, float | Any, float | Any]:
    """Принимает транзакции и возвращает их сумму"""
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
    print(round(total_sum_rub,2), round(total_sum_usd,2), round(total_sum_eur,2))
    return total_sum_rub, total_sum_usd, total_sum_eur


def currency_exchange(total_sum_usd, total_sum_eur):
    """Конвертование валюты с USD, EUR"""
    API_KEY = 'NnFGX1wy9tQ8PNdlD9f91cB3aa8LuThr'
    url_for_usd = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={total_sum_usd}"
    url_for_eur = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={total_sum_eur}"

    payload = {}
    headers = {"apikey": "NnFGX1wy9tQ8PNdlD9f91cB3aa8LuThr"}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    print(result)


if __name__ == "__main__":
    transactions_sum(file="D:\\PythonProject\\PythonProject_NPR\\data/operations.json")
