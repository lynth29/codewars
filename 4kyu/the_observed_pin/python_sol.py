from itertools import *
def get_pins(observed):
    # Create a dictionary for all possible number for each number
    a_dict = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'], '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9'], '0': ['0', '8']}
    # Make a list of all possible lists
    lst = [a_dict[i] for i in observed]
    # Use itertools.product to make combinations
    result = list(product(*lst))
    # Concanate number into strings
    answer = [''.join(x) for x in result]
    return answer
