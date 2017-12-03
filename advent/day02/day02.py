def calculate_checksum(txt):
    rows = txt.split("\n")
    total = 0

    for row in rows:
        nums = [int(x) for x in row.split()]
        total += max(nums) - min(nums)

    return total

def find_divisble_pair(arr):
    ordered = sorted(arr, reverse=True)
    for idx, num in enumerate(ordered):
        offset = idx + 1
        for other in ordered[offset:]:
            if num % other == 0:
                return int(num / other)

    return 0


def calculate_checksum_two(txt):
    rows = txt.split("\n")
    total = 0

    for row in rows:
        nums = [int(x) for x in row.split()]
        total += find_divisble_pair(nums)

    return total
