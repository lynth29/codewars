"""
Implement a function that adds two numbers together
and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    return str(bin(a+b)[2:])

# second solution
# from zebulan@codewars
def add_binary_2nd(a,b):
    return format(a + b, 'b')
    # 'b' there stands for 'binary'.
    # so basically it will return the sum in binary format
