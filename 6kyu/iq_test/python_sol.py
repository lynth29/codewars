"""
Bob is preparing to pass IQ test.
The most frequent task in this test is to find out
which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among
the given numbers finds one that is different in evenness,
and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

Given numbers: "2 4 7 8 10"
"""

def iq_test(numbers):
    numbers = numbers.split(' ')
    odd = [num for num in numbers if int(num) % 2]
    even = [num for num in numbers if num not in odd]
    if len(odd) == 1:
        for i in odd:
            return(numbers.index(i) + 1)
    else:
        for i in even:
            return(numbers.index(i) + 1)

# second solution
def iq_test_second(numbers):
    odd = [int(i) % 2 for i in numbers.split(' ')]
    return odd.index(1)+1 if odd.count(1) == 1 else odd.index(0)+1
