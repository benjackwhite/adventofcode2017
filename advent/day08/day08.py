import re

line_regex = re.compile("^([a-z]+) ([a-z]+) (-?\d+) if ([a-z]+) ([><=!]+) (-?\d+)$")


def check_condition(left_value, comparison, value):
    if comparison == "==":
        return left_value == value
    if comparison == "!=":
        return left_value != value
    if comparison == "<=":
        return left_value <= value
    if comparison == ">=":
        return left_value >= value
    if comparison == "<":
        return left_value < value
    if comparison == ">":
        return left_value > value

    raise Exception("Unknown operator: {}".format(comparison))

def execute_instructions(txt):
    registers = {}
    memory = {
        "__largest": None,
        "__smallest": None,
        "registers": registers
    }
    
    lines = txt.split("\n")

    for line in lines:
        matches = line_regex.match(line)

        register = matches.group(1)
        action = matches.group(2)
        amount = int(matches.group(3))
        condition_register = matches.group(4)
        condition_comparison = matches.group(5)
        condition_value = int(matches.group(6))

        if register not in registers:
            registers[register] = 0
        if condition_register not in registers:
            registers[condition_register] = 0

        if check_condition(registers[condition_register], condition_comparison, condition_value):
            if action == "inc":
                registers[register] += amount
            elif action == "dec":
                registers[register] -= amount

            if not memory["__largest"] or registers[register] > memory["__largest"]:
                memory["__largest"] = registers[register]
            
            if not memory["__smallest"] or registers[register] < memory["__smallest"]:
                memory["__smallest"] = registers[register]

    return memory
