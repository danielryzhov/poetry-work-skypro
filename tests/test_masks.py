import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [('7000792289606361', '7000 79** **** 6361'), ('7010752289606361', '7010 75** **** 6361'), ('7000792289605555', '7000 79** **** 5555')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number_negative", [('700079228960636'),('70007922896063611'),('a000792289606361'), ('helloworldqwerty'), (' '), ('') ])
def test_get_mask_card_number_negative(card_number_negative):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number_negative)

    assert str(exc_info.value) == "Invalid account number"

@pytest.mark.parametrize("account, expected_acc", [('73654108430135874305','**4305'), ('73654108430135875555', '**5555'),('13654188530135874305', '**4305')])
def test_get_mask_account(account, expected_acc):
    assert get_mask_account(account) == expected_acc

@pytest.mark.parametrize("account_negative", [('7365410843013587430'),('736541084301358743054'),('7a654108430135874305'), ('helloworldqwerty'), (' '), ('') ])
def test_get_mask_account_negative(account_negative):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_negative)

    assert str(exc_info.value) == "Invalid account number"
