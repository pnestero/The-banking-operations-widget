def get_mask_card_number(number_card: int) -> str:
    """маскировка номера банковской карты"""
    number_card_str = str(number_card)
    if len(number_card_str) != 16:
        raise ValueError("Неправильный номер карты")
    result = f"{number_card_str[0:4]} {number_card_str[4:6]}** **** {number_card_str[-4:]}"
    return result


def get_mask_account(number_account: int) -> str:
    """маскировка номера банковского счета"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        raise ValueError("Неправильный номер аккаунта")
    result = f"**{number_account_str[-4:]}"
    return result


if __name__ == "__main__":
    # number_card_1 = int(input("Enter card number: ")) Для ввода вручную
    # number_account = int(input("Enter account number: ")) Для ввода вручную

    number_card_1 = 1234123412341234
    number_account = 73654108430135874305
    print(get_mask_card_number(number_card_1))
    print(get_mask_account(number_account))
