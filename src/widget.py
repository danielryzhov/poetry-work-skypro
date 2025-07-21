from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция принимает на вход номер счета или карты и возвращает их маску"""
    name, number = account_card.rsplit(" ", maxsplit=1)
    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{name} {masked_number}"


def get_date(date: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    2024-03-11T02:26:18.671407 и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if date == "":
        return ""
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
