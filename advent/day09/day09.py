def count(txt):
    groups_total = 0
    current_groups = 0
    in_garbage = False
    in_group = False
    garbage_count = 0

    count = -1

    while count + 1 < len(txt):
        count += 1

        c = txt[count]

        if txt[count] == "!":
            count += 1
        elif not in_garbage and c == "<":
            in_garbage = True

        elif c == ">":
            in_garbage = False

        elif in_garbage:
            garbage_count += 1

        elif not in_garbage:
            if c == "{":
                current_groups += 1

            elif c == "}":
                groups_total += current_groups
                current_groups -= 1

    return groups_total, garbage_count

def count_groups(txt):
    return count(txt)[0]

def count_garbage(txt):
    return count(txt)[1]
