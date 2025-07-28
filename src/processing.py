from typing import Any, Iterable


def filter_by_state(filter_state: list[dict], state="EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает новый список словарей содержащий только
    те словари, у которых ключ state соответствует указанному значению"""

    new_filter_state = []
    for dictionary_state in filter_state:
        if dictionary_state["state"] == state:
            new_filter_state.append(dictionary_state)
    return new_filter_state


def sort_by_date(sort_date: list[dict], reverse=True) -> list[dict]:
    """Функция принимает список словарей и возвращает новый список отсортированный по дате"""
    sorted_date = sorted(sort_date, key=lambda dictionary_date: dictionary_date["date"], reverse=reverse)
    return sorted_date
