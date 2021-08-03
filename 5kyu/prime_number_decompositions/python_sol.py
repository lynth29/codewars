from collections import Counter

def getAllPrimeFactors(n):
    arr = []
    i = 2
    if (type(n) != int) or (n <= 0):
        return []
    elif n == 1:
        return [1]
    else:
        while i <= n:
            if n % i == 0:
                arr.append(i)
                n = n / i
            else:
                i += 1
        return sorted(arr)

def getUniquePrimeFactorsWithCount(n):
    if (type(n) != int) or (n <= 0):
        return [[],[]]
    else:
        arr = getAllPrimeFactors(n)
        items = Counter(arr)
        factor = []
        count = []
        for k, v in items.items():
            factor.append(k)
            count.append(v)
        return [factor, count]

def getUniquePrimeFactorsWithProducts(n):
    if (type(n) != int) or (n <= 0):
        return []
    else:
        arr = getAllPrimeFactors(n)
        items = Counter(arr)
        return [k**v for k, v in items.items()]
