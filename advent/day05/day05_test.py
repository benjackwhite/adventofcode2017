from day05 import reach_exit, reach_exit_two
from data import data


target_list = [int(x) for x in data.split("\n")]

def test_reach_exit():
    assert reach_exit([0,3,0,1,-3]) == 5
    assert reach_exit(target_list) == 372139


def test_reach_exit_two():
    assert reach_exit_two([0, 3, 0, 1, -3]) == 10
    assert reach_exit_two(target_list) == 29629538

