from functools import reduce


def get_circular_index(arr, index):
    if index >= len(arr):
        while index >= len(arr):
            index -= len(arr)

    return index


def circular_move(arr, pos, amount):
    index = pos + amount
    while index >= len(arr):
        index -= len(arr)

    return index


def fn(arr, twists, pos = 0, skip_size = 0):
    arr = arr[:]
    current = []

    for t in twists:
        for i in range(t):
            index = get_circular_index(arr, pos + i)
            current.append(arr[index])

        current.reverse()
        for i in range(t):
            index = get_circular_index(arr, pos + i)
            arr[index] = current[i]

        pos = circular_move(arr, pos, t + skip_size)
        skip_size += 1
        if skip_size >= len(arr):
            skip_size -= len(arr)

    return arr, pos, skip_size


def knot_hash(arr, txt):
    pos = 0
    skip_size = 0
    current = []
    standard_twists = [17, 31, 73, 47, 23]

    twists = [ord(c) for c in list(txt)] + standard_twists

    # print(twists)

    for i in range(64):
        # print(pos, skip_size)
        mashed, new_pos, new_skip_size = fn(arr, twists, pos, skip_size)

        # print(new_pos, new_skip_size)
        pos = new_pos
        skip_size = new_skip_size

    dense = []

    for i in range(16):
        block = mashed[i:i+16]
        current = 0

        product = reduce((lambda x, y: x ^ y), block)
        dense.append(product)


    print(dense)
    dense = ['{0:02x}'.format(x) for x in dense]
    print(dense)

    return "".join(dense)
