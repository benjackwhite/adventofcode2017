def find(arr, fn):
    for index, item in enumerate(arr):
        if fn(item):
            return index, item


def balance_banks(arr, loops = 1):
    arr = arr[:]
    steps = 0
    seen = {}

    while True:
        steps += 1

        biggest = max(arr)
        index, _ = find(arr, lambda x: x == biggest)
        arr[index] = 0

        index += 1

        for i in range(biggest):
            pos = (i + index) % len(arr)
            arr[pos] += 1

        key = ",".join([str(x) for x in arr])
        key_val = seen.get(key, 0)
        if key_val == loops:
            return steps
        else:
            seen[key] = key_val + 1
