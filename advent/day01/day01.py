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
