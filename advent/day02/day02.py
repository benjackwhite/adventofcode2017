def calculate_checksum(txt):
    rows = txt.split("\n")
    total = 0

    for row in rows:
        nums = [int(x) for x in row.split()]
        total += max(nums) - min(nums)

    return total
