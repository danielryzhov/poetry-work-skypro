import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(by_transactions):
    generator_filter_by_currency = filter_by_currency(by_transactions, "USD")
    assert next(generator_filter_by_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator_filter_by_currency) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator_filter_by_currency) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_no_transactions(by_transactions):
    generator_no_transactions = filter_by_currency(by_transactions, "yuan")
    list_empty = []
    assert list(generator_no_transactions) == []
    assert list(filter_by_currency(list_empty)) == []


@pytest.mark.parametrize(
    "transactions_description, expected",
    [({
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }, "Перевод организации"), ({
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }, "Перевод со счета на счет"), ({
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }, "Перевод с карты на карту")])
def test_transaction_descriptions(transactions_description, expected):
    generator_transaction_descriptions = transaction_descriptions([transactions_description])
    assert next(generator_transaction_descriptions) == expected


def test_transaction_descriptions(by_transactions):
    generator_transaction_descriptions = transaction_descriptions(by_transactions)
    list_empty = []
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод с карты на карту"
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert list(transaction_descriptions(list_empty)) == []


def test_card_number_generator():
    assert list(card_number_generator(1, 5)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
