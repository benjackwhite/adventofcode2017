from day09 import count_groups, count_garbage
from data import data


def test_count_groups():
    assert count_groups("{}") == 1
    assert count_groups("{{{}}}") == 6
    assert count_groups("{{},{}}") == 5
    assert count_groups("{{{},{},{{}}}}") == 16
    assert count_groups("{<a>,<a>,<a>,<a>}") == 1
    assert count_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert count_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert count_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

    assert count_groups(data) == 14190


def test_count_garbage():
    assert count_garbage('<>') == 0
    assert count_garbage('<random characters>') == 17
    assert count_garbage('<<<<>') == 3
    assert count_garbage('<{!>}>') == 2
    assert count_garbage('<!!>') == 0
    assert count_garbage('<!!!>>') == 0
    assert count_garbage('<{o"i!a,<{i<a>') == 10
    assert count_garbage(data) == 7053
