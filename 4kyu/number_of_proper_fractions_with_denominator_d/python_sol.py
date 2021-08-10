import math
def proper_fractions(n):
    if n == 1:
        return 0
    result, a = n, n
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            while a % i == 0:
                a /= i
            result = result / i * (i-1)
    if a > 1:
        result = result / a * (a-1)
    return result
