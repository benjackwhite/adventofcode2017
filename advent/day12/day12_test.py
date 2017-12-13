from day12 import fn, fn2
from data import data

test_case = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

def test_fn():
    assert fn(test_case) == 6 
    assert fn(data) == 130


def test_fn2():
    assert fn2(test_case) == 2
    assert fn2(data) == 189
