def solve_runes(runes):
    numeric = set("0123456789")
    for d in sorted(numeric - set(runes)):
        test = runes.replace("?", d).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any(i[0] == '0' and i != '0' for i in test.split()) and eval(test):
            return int(d)
    return -1 
