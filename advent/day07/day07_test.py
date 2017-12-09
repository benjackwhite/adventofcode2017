from day07 import find_bottom, find_weight_change
from data import data


example_data = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""



def test_find_bottom():
    assert find_bottom(example_data) == "tknk"
    assert find_bottom(data) == "svugo"


def test_find_weight_change():
    assert find_weight_change(example_data) == 60
    # assert find_weight_change(data) == "svugo"
