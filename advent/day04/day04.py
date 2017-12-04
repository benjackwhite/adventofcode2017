def check_passphrase(txt):
    parts = txt.split()
    index = {}

    for p in parts:
        if p in index:
            return False
        index[p] = True
    
    return True
    
def check_passphrase_two(txt):
    parts = txt.split()
    index = {}

    for p in parts:
        sorted_p = ''.join(sorted(p))
        if sorted_p in index:
            return False
        index[sorted_p] = True

    return True
