from day03 import calculate_distance, calculate_next_large_value

target = 325489

def test_calculate_distance():
    assert calculate_distance(1) == 0
    assert calculate_distance(12) == 3
    assert calculate_distance(23) == 2
    assert calculate_distance(1024) == 31

    assert calculate_distance(target) == 552


def test_calculate_next_large_value():
    assert calculate_next_large_value(1) == 2
    assert calculate_next_large_value(2) == 4
    assert calculate_next_large_value(10) == 11
    assert calculate_next_large_value(133) == 142

    assert calculate_next_large_value(target) == 330785
