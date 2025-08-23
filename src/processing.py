def filter_by_state(users_id: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и возвращает словарь,
    с ключом по умолчанию "EXECUTED". """
    filter_by_list = []
    for user_id in users_id:
        if user_id.get("state") == state:
            filter_by_list.append(user_id)
        else:
            continue

    return filter_by_list


def sort_by_date(users_id: list[dict], decreasing: bool = True) -> list[dict]:
    """ Сортировка по дате операции"""
    sorted_by_list_date = sorted(users_id, key=lambda x: x.get("date", ""), reverse=decreasing)
    return sorted_by_list_date


if __name__ == "__main__":
    test_list = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    test_1 = filter_by_state(test_list, state="CANCELED")
    print(test_1)
