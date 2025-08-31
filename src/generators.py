def filter_by_currency(transactions, code="USD"):
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(number=1, end_card=9999999999999999):
    """Генератор card_number_generator, который выдает номера банковских карт
     в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    while number <= end_card:
        number_line = str(number)
        card_number = number_line.zfill(16)
        number += 1
        card_number_line = str(card_number)
        yield f"{card_number_line[0:4]} {card_number_line[4:8]} {card_number_line[8:12]} {card_number_line[12:16]}"
