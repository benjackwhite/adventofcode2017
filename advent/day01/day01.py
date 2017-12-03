def reverse_captcha(txt):
    arr = [int(x) for x in list(txt)]
    total = 0
    previous = None

    for c in arr:
        if c == previous:
            total += c

        previous = c

    if arr[0] == arr[-1]:
        total += arr[0]

    return total


def reverse_captcha_two(txt):
    arr = [int(x) for x in list(txt)]
    arr_length = len(arr)
    half_way = int(arr_length * 0.5)
    total = 0

    for idx, c in enumerate(arr):
        pointer = idx + half_way
        if pointer >= arr_length:
            pointer -= arr_length
        
        if arr[pointer] == c:
            total += c

    return total
