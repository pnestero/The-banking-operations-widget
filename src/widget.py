from src.masks import get_mask_card_number, get_mask_account
import datetime

def mask_card_number(sistem_number_card: str) -> str:
    """Маскировка карты"""
    if "Счет" in sistem_number_card:
        sistem_card_str = f"{sistem_number_card[:-21]}"
        number_card_str = f"{sistem_number_card[-20:]}"
        number_card_str = get_mask_account(number_card_str)
        return f'{sistem_card_str} {number_card_str}'
    else:
        sistem_card_str = f"{sistem_number_card[:-16]}"
        number_card_str = f"{sistem_number_card[-16:]}"
        number_card_str = get_mask_card_number(number_card_str)
        return f'{sistem_card_str} {number_card_str}'



print(mask_card_number("Visa Platinum 7000792289606361"))
print(mask_card_number("Счет 64686473678894779589"))

from datetime import datetime


def get_date(date_str):
    date_obj = datetime.fromisoformat(date_str)
    # Переводим в формат "ДД.ММ.ГГГГ"
    formatted_date = date_obj.strftime('%d.%m.%Y')
    return formatted_date

input_date = "2024-03-11T02:26:18.671407"
output_date = get_date(input_date)
print(output_date)




# #Пользователь вводит номер карты по представленному формату
# card_and_numder = input("""Введите номер счёта или номер карты
# (например:
# Счет 73654108430135874305
# Maestro 1596837868705199
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Gold 5999414228426353)\n""")
#
# card_numder = card_and_numder.strip(" ")
# for numder in card_numder:
#     print(mask_card_number(numder))
