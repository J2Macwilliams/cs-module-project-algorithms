'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time

start_time = time.time()

def sliding_window_max(nums, k):
    # Plan
    # create a new_array
    new_array = []
    # set start
    start = 0
    end = k
    # check for base case 
    # k contains certain indices
    # k increments 1 indice at a time
    # numbers have a start and an end 
    #  use some sort of iterator I guess
    # k must be smaller  or equal than nums
    while end <= len(nums): # O(n)
        # window is a slice of nums 
        new_array.append(max(nums[start:end]))
        # increment start and end
        start += 1
        end += 1
    
    # return max items
    return new_array

end_time = time.time()

sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) 

print(f"runtime: {end_time - start_time} seconds")

#First Pass
# runtime: 2.1457672119140625e-06 seconds
# Runtime complexity: O(n^2), however the second (n) is based off the size of k which dramatically shortens the time.

# Better Solution
# runtime: 1.1920928955078125e-06 seconds
# Runtime Complexity: O(n)

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
