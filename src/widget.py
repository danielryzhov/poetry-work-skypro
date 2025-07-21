import masks
def mask_account_card(masks_account_card: str) -> str:
    '''Функция принимает на вход номер счета или карты и возвращает их маску'''

    bank_account = 'Счет'
    index_card = masks_account_card.find(bank_account)
    list_account_card = masks_account_card.split(' ')
    if index_card == -1:
        list_account_card[-1] = masks.get_mask_card_number(list_account_card[-1])
        masks_account_card = " ".join(list_account_card)
        return masks_account_card
    else:
        list_account_card[-1] = masks.get_mask_account(list_account_card[-1])
        masks_account_card = " ".join(list_account_card)
        return masks_account_card


def get_date(date: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    2024-03-11T02:26:18.671407 и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if date == '':
        return ''
    else:
        return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'

