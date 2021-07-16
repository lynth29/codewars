"""Perfect Power is a positive integer that can be expressed as an integer
power of another positive integer.
In short, n is a perfect power if there exist natural numbers m > 1,
k > 1 and m**k == n"""

from math import sqrt
def isPP(n):
    """Return m,k with m**k ==n if n is a perfect power otherwise return None."""
    m = int(sqrt(n))
    for i in range(2, m+1):
        k = 0
        while i**k < n:
            k+=1
        if i**k == n:
            return [i, k]
    return None
