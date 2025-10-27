from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_card_number(sistem_number_card: str) -> str:
    """Маскировка карты и счета"""
    if "Счет" in sistem_number_card:
        sistem_card_str = sistem_number_card[:-20].strip()
        number_card_str = sistem_number_card[-20:]
        number_card_str = get_mask_account(int(number_card_str))
        return f"{sistem_card_str} {number_card_str}"
    else:
        sistem_card_str = sistem_number_card[:-16].strip()
        number_card_str = sistem_number_card[-16:]
        number_card_str = get_mask_card_number(int(number_card_str))
        return f"{sistem_card_str} {number_card_str}"


def get_date(date_str: str) -> str:
    """Форматирование даты в формат ДД.ММ.ГГГГ"""
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
