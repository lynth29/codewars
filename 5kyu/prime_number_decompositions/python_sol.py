from collections import Counter

def getAllPrimeFactors(n):
    arr = []
    i = 2
    if (n <= 0) or type(n) != 'int':
        return []
    else:
        while i <= n:
            print(f"With i = {i} and n = {n}")
            if n % i == 0:
                print(f"{n} % {i} so let's append it to the array")
                arr.append(i)
                n = n / i
                print(f"now n = {n}")
            else:
                print(f"It's not prime factors, skip")
                i += 1
        return sorted(arr)

def getUniquePrimeFactorsWithCount(n):
    if (n <= 0) or type(n) != 'int':
        return [[],[]]]
    else:
        arr = getAllPrimeFactors(n)
        items = Counter(arr)
        factor = []
        count = []
        for k, v in items.items():
            factor.append(k)
            count.append(v)
        return [factor, count]

def getUniquePrimeFactorsWithProducts():
    if (n <= 0) or type(n) != 'int':
        return []
    else:
        arr = getAllPrimeFactors(n)
        items = Counter(arr)
        return [k**v for k, v in items.items()]

arr = []
n = 1
i = 1
if (n <= 0) or type(n) != 'int':
    arr = []
elif n == 1:
    arr = [1]
else:
    while i <= n:
        print(f"With i = {i} and n = {n}")
        if n % i == 0:
            print(f"{n} % {i} so let's append it to the array")
            arr.append(i)
            n = n / i
            print(f"now n = {n}")
        else:
            print(f"It's not prime factors, skip")
            i += 1
arr
from itertools import *
items = Counter(arr)
items
[k**v for k, v in items.items()]
lst = []
factor = []
count = []
for k, v in items.items():
    factor.append(k)
    count.append(v)
factor
count
lst = [factor, count]

lst
n
type(n)
