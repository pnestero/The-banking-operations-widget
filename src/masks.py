def get_mask_card_number(number_card: int) -> str:
    """Маскировка номера банковской карты
    :rtype: str
    """
    number_card_str = str(number_card)
    number_card_str = number_card_str.replace(" ", "")
    if len(number_card_str) != 16:
        raise ValueError("Неправильный номер карты")
    elif not number_card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    result = f"{number_card_str[0:4]} {number_card_str[4:6]}** **** {number_card_str[-4:]}"
    return result


def get_mask_account(number_account: int) -> str:
    """Маскировка номера банковского счета"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        raise ValueError("Неправильный номер аккаунта")
    elif not number_account_str.isdigit():
        raise ValueError("Номер аккаунта должен содержать только цифры")
    result = f"**{number_account_str[-4:]}"
    return result


if __name__ == "__main__":
    # number_card_1 = int(input("Enter card number: ")) #Для ввода вручную
    # number_account = int(input("Enter account number: ")) #Для ввода вручную

    number_card_1 = 1111222233334444
    number_account = 73654108430135874305
    print(get_mask_card_number(number_card_1))
    print(get_mask_account(number_account))
