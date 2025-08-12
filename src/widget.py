from src.masks import get_mask_card_number, get_mask_account


def mask_card_number(sistem_number_card: str) -> str:
    """Маскировка карты"""
    if (("Счёт" in sistem_number_card) or ("счёт" in sistem_number_card)
    or ("Cчет" in sistem_number_card) or ("счет" in sistem_number_card)):
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
