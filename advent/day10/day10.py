def get_circular_index(arr, index):
    if index >= len(arr):
        return index - len(arr)

    return index


def circular_move(arr, pos, amount):
    new_index = pos + amount
    if new_index >= len(arr):
        return new_index - len(arr)

    return new_index


def fn(arr, twists):
    pos = 0
    skip_size = 0
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


    return arr
