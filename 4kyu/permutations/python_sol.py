import itertools

def permutations(string):
    p = itertools.permutations(string)
    return [''.join(i) for i in (set(p))]
