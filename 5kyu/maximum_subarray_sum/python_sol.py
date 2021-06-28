"""
The maximum sum subarray problem consists in finding the maximum sum of
a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers
and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum.
Note that the empty list or array is also a valid sublist/subarray.
"""
def max_sequence(arr):
    # Assign current sum as 0
    curr_sum = 0
    # Assign most possible maximum sum as 0
    max_sum = 0
    # If the list is empty then max_sum == 0, use len(arr)
    if len(arr) == 0:
        max_sum = 0
    else:
        # for loop to run through each number in the array
        for i in arr:
            curr_sum += i
            # if the number is negative, the current sum will be returned to 0
            # so we can calculate the maximum easily
            if curr_sum < 0:
                curr_sum = 0
            # define the maximum sum through each number    
            elif max_sum < curr_sum:
                max_sum = curr_sum
    return max_sum
