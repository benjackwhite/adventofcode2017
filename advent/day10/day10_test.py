from day10 import fn, knot_hash

arr256 = [x for x in range(256)]


def test_fn():
    changed = fn([0, 1, 2, 3, 4], [3, 4, 1, 5])[0]

    assert changed[0] * changed[1] == 12

    changed = fn(
        arr256,
        [102, 255, 99, 252, 200, 24, 219, 57, 103, 2, 226, 254, 1, 0, 69, 216]
    )[0]

    assert changed[0] * changed[1] == 5577


def test_knot_hash():
    assert knot_hash(arr256, "1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert knot_hash(arr256, "") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert knot_hash(arr256, "AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert knot_hash(arr256, "1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
    
    assert knot_hash(
        arr256,
        "102, 255, 99, 252, 200, 24, 219, 57, 103, 2, 226, 254, 1, 0, 69, 216"
    ) == "wat"
