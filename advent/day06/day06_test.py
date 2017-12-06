from day06 import balance_banks, balance_banks_two


target_banks = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]


def test_balance_banks():
    assert balance_banks([0,2,7,0]) == 5
    assert balance_banks(target_banks) == 4074


def test_balance_banks_two():
    assert balance_banks([0, 2, 7, 0], 2) - balance_banks([0, 2, 7, 0], 1) == 4
    assert balance_banks(target_banks, 2) - balance_banks(target_banks, 1) == 4074
