"""
Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum.
"""
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

def sum_pairs(ints, s):
    seen = set()
    for num in ints:
        print(num, s - num, seen)
        if s - num in seen:
            return [s - num, num]
        seen.add(num)
