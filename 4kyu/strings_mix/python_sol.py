from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    substr = []
    for c in list(set(c1.keys())|set(c2.keys())):
        n1, n2 = c1.get(c,0), c2.get(c,0)
        if n1 > 1 or n2 > 1:
            if n1 > n2:
                substr.append((f"1:{c*n1}"))
            elif n1 < n2:
                substr.append((f"2:{c*n2}"))
            else:
                substr.append((f"=:{c*n1}"))
    substr = sorted(substr, key=lambda x: (-len(x), x))
    return '/'.join(substr)
