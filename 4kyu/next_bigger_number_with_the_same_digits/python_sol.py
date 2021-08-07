# My solution, use itertools.permutations but timed out
from itertools import permutations

def next_bigger(n):
    if n < 10:
        return -1
    p = permutations(str(n))
    lst = []
    for i in list(p):
        num = int(''.join(i))
        if num > n:
            lst.append(num)
    return -1 if len(lst) == 0 else lst[0]

# not timed out solution
def next_bigger(n):
    max = int(''.join(sorted(str(n))[::-1]))
    if n == max:
        return -1
    temp = sorted(str(n))
    for digit in range(n+1, max+1):
        if sorted(str(digit)) == temp:
            return digit
