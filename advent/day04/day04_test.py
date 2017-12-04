from day04 import check_passphrase, check_passphrase_two
from data import data


def test_check_passphrase():
    assert check_passphrase("aa bb cc dd ee")
    assert not check_passphrase("aa bb cc dd aa")
    assert check_passphrase("aa bb cc dd aaa")

    rows = data.split("\n")

    num = len([x for x in rows if check_passphrase(x) ])

    assert num == 451


def test_check_passphrase_two():
    assert check_passphrase_two("abcde fghij")
    assert not check_passphrase_two("abcde xyz ecdab")
    assert check_passphrase_two("a ab abc abd abf abj")
    assert check_passphrase_two("iiii oiii ooii oooi oooo")
    assert not check_passphrase_two("oiii ioii iioi iiio")
    
    rows = data.split("\n")

    num = len([x for x in rows if check_passphrase_two(x)])

    assert num == 223
