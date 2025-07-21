def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    if not (card_number.isdigit() and len(card_number) == 16):
        raise ValueError("Invalid account number")
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if not (account.isdigit() and len(account) == 20):
        raise ValueError("Invalid account number")
    return f"{'*' * 2}{account[16:]}"
