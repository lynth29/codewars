"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(string):
    unique = sorted(list(set(string)))
    result = []
    for char in unique:
        count = string.count(char)
        result.append(count)
    return dict(zip(unique, result))

# better solution
def count_second(string):
    return {i: string.count(i) for i in dict.fromkeys(string)}
