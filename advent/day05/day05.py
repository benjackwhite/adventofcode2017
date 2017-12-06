def reach_exit(arr):
    arr = arr[:]
    steps = 0
    index = 0

    while index >= 0 and index < len(arr):
        last_index = index
        index += arr[index]
        arr[last_index] += 1
        steps += 1

    return steps


def reach_exit_two(arr):
    arr = arr[:]
    steps = 0
    index = 0

    while index >= 0 and index < len(arr):
        offset = arr[index]
        if offset >= 3:
            arr[index] -= 1
        else:
            arr[index] += 1

        index += offset
        steps += 1

    return steps
