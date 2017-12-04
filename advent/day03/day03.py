from collections import OrderedDict

def manhattan_distance(start, end):
    start_x, start_y = start
    end_x, end_y = end
    return abs(end_x - start_x) + abs(end_y - start_y)

def create_spiral(start=1, end= 1000):
    ''' Creates an object representing the spiral structure.
    Starting with a direction (0=East, 1=North, 2=West, 3=South) it constructs
    the object
    '''
    direction = 0
    pointer = (0, 0)
    corners = [0, 0, 0, 0]
    spiral = OrderedDict({
        start: pointer
    })

    for i in range(start + 1, end + 1):
        if direction == 0:
            pointer = (pointer[0] + 1, pointer[1])
            if pointer[0] > corners[direction]:
                direction = 1
        elif direction == 1:
            pointer = (pointer[0], pointer[1] - 1)
            if pointer[1] < corners[direction]:
                direction = 2
        elif direction == 2:
            pointer = (pointer[0] - 1, pointer[1])
            if pointer[0] < corners[direction]:
                direction = 3
        elif direction == 3:
            pointer = (pointer[0], pointer[1] + 1)
            if pointer[1] > corners[direction]:
                direction = 0

        if pointer[0] > corners[0]:
            corners[0] = pointer[0]
        if pointer[1] < corners[1]:
            corners[1] = pointer[1]
        if pointer[0] < corners[2]:
            corners[2] = pointer[0]
        if pointer[1] > corners[3]:
            corners[3] = pointer[1]

        spiral[i] = pointer

    return spiral

def calculate_distance(target, entry=1):
    spiral = create_spiral(start=entry, end=target)

    return manhattan_distance(spiral[entry], spiral[target])


def calculate_next_large_value(target, entry=1):
    spiral = create_spiral(start=entry, end=target + 10)
    reverse_spiral = { value: key for key, value in spiral.items() }

    new_spiral = OrderedDict()

    for v, pos in spiral.items():
        if pos == (0,0):
            new_spiral[pos] = v
            continue
        value = 0

        value += new_spiral.get((pos[0] - 1, pos[1] - 1), 0)
        value += new_spiral.get((pos[0] - 1, pos[1]), 0)
        value += new_spiral.get((pos[0], pos[1] - 1), 0)
        value += new_spiral.get((pos[0] + 1, pos[1] + 1), 0)
        value += new_spiral.get((pos[0] + 1, pos[1]), 0)
        value += new_spiral.get((pos[0], pos[1] + 1), 0)
        value += new_spiral.get((pos[0] - 1, pos[1] + 1), 0)
        value += new_spiral.get((pos[0] + 1, pos[1] - 1), 0)

        new_spiral[pos] = value

    vals = sorted([v for k, v in new_spiral.items()])

    for idx, v in enumerate(vals):
        if v > target:
            return v

    return 0
