# My solution
def snail(snail_map):
    # Create an empty list to store answer
    expected = []
    # Create a while loop to add element into answer list
    i = 1
    n = len(snail_map)
    while i <= n:
        # Add even row
        if i % 2 != 0:
            expected.extend(snail_map[0])
            snail_map.pop(0)
            # Add right column
            for line in snail_map:
                expected.append(line[-1])
                line.pop(-1)
        # Add odd row
        elif i % 2 == 0:
            expected.extend(reversed(snail_map[-1]))
            snail_map.pop(-1)
            # Add left column
            for line in reversed(snail_map):
                expected.append(line[0])
                line.pop(0)
        # Add last row
        elif i == n:
            expected.extend(snail_map[0])
            snail_map.pop()
        i+=1
    return expected



# Clever solution
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
