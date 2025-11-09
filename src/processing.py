def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует транзакции по статусу.
    Работает с разными форматами данных (JSON, CSV, Excel).

    :param transactions: Список словарей с транзакциями
    :param state: Статус для фильтрации (EXECUTED, CANCELED, PENDING)
    :return: Отфильтрованный список транзакций
    """

    if transactions is None:
        print("Не передан список транзакций")
        return []

    filter_by_list = []
    state_lower = state.lower()

    for transaction in transactions:
        # Пропускаем элементы, которые не являются словарями
        if not isinstance(transaction, dict):
            continue

        # Ищем ключ статуса в разных вариантах для разных форматов файлов
        state_value = None

        # Для JSON файлов обычно "state"
        # Для CSV/Excel файлов могут быть разные названия
        possible_status_keys = ["state", "State", "STATE"] # на русском, если файлы локализованы

        for key in possible_status_keys:
            if key in transaction and transaction[key] is not None:
                state_value = str(transaction[key]).strip()
                break

        # Если не нашли стандартными ключами, ищем по частичному совпадению
        if state_value is None:
            for key in transaction.keys():
                if "state" in key.lower() or "status" in key.lower():
                    state_value = str(transaction[key]).strip()
                    break

        # Проверяем совпадение статуса
        if state_value is not None and state_value.lower() == state_lower:
            filter_by_list.append(transaction)

    return filter_by_list


def sort_by_date(users_id: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка по дате операции"""
    if users_id is None:
        return []
    sorted_by_list_date = sorted(users_id, key=lambda x: x.get("date", ""), reverse=reverse)

    return sorted_by_list_date


if __name__ == "__main__":
    test_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    test_1 = filter_by_state(test_list, state="CANCELED")
    print(test_1)

# def filter_by_state(users_id: list[dict], state: str = "EXECUTED") -> list[dict]:
#     """Принимает список словарей и возвращает словарь,
#     с ключом по умолчанию "EXECUTED"."""
#
#     if users_id is None:
#         print("Не передан список словарей")
#         return []
#
#     filter_by_list = []
#     state_lower = state.lower()
#
#     for user_id in users_id:
#         state_value = user_id.get("state")
#         if state_value is not None and str(state_value).lower() == state_lower:
#            filter_by_list.append(user_id)
#
#
#     return filter_by_list