import math

from day08 import execute_instructions
from data import data


def highest(d):
    largest = None
    key = None

    for k, v in d.items():
        if largest is None or v > largest:
            largest = v
    
    return largest

def test_execute_instructions():
    assert highest(execute_instructions("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""")["registers"]) == 1

    assert highest(execute_instructions(data)["registers"]) == 3745


def test_execute_instructions_largest_ever():
    assert execute_instructions("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""")["__largest"] == 10

    assert execute_instructions(data)["__largest"] == 4644
