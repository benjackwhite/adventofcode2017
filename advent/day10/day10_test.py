from day10 import fn
from data import data

arr256 = [x for x in range(256)]


def test_fn():
    changed = fn([0, 1, 2, 3, 4], [3, 4, 1, 5])

    assert changed[0] * changed[1] == 12

    changed = fn(
        arr256,
        [102, 255, 99, 252, 200, 24, 219, 57, 103, 2, 226, 254, 1, 0, 69, 216]
    )

    assert changed[0] * changed[1] == 5577
