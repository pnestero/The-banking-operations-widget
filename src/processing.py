def filter_by_state(users_id: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и возвращает словарь,
    с ключом по умолчанию "EXECUTED"."""

    if users_id is None:
        print("Не передан список словарей")
        return []

    filter_by_list = []
    state_lower = state.lower()

    for user_id in users_id:
        state_value = user_id.get("state")
        if state_value is not None and str(state_value).lower() == state_lower:
            filter_by_list.append(user_id)

    return filter_by_list


def sort_by_date(users_id: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка по дате операции"""
    if users_id is None:
        return []
    sorted_by_list_date = sorted(users_id, key=lambda x: x.get("date", ""), reverse=reverse)

    return sorted_by_list_date
