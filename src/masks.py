import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(r"D:\PythonProject\PythonProject_NPR\logs\masks.log", "w", "utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int | str) -> str:
    """Маскировка номера банковской карты
    :rtype: str
    """
    number_card_str = str(number_card)
    number_card_str = number_card_str.replace(" ", "")
    if len(number_card_str) != 16:
        logger.error(f"Неправильный номер карты: {number_card_str}")
        return "Ошибка: номер карты должен содержать 16 цифр"
    elif not number_card_str.isdigit():
        logger.error(f"Номер карты должен содержать только цифры: {number_card_str}")
        return "Ошибка: номер карты должен содержать только цифры"
    masked_number = f"{number_card_str[0:4]} {number_card_str[4:6]}** **** {number_card_str[-4:]}"
    logger.info(f"Карта замаскирована: {masked_number}")
    return masked_number


def get_mask_account(number_account: int | str) -> str:
    """Маскировка номера банковского счета"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        logger.error(f"Неправильный номер аккаунта: {number_account_str}")
        return "Ошибка: номер счёта должен содержать 20 цифр"
    elif not number_account_str.isdigit():
        logger.error(f"Номер аккаунта должен содержать только цифры: {number_account_str}")
        return "Ошибка: номер счёта должен содержать только цифры"
    masked_account = f"**{number_account_str[-4:]}"
    logger.info(f"Счёт замаскирован: {masked_account}")  # // ИСПРАВЛЕНО: error → info
    return masked_account
