'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
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
    while end <= len(nums):
        # k is a slice of nums
        my_window = [ x for x in nums[start:end]]
        # max identifies the highest
        my_max = max(my_window)
        new_array.append(my_max)
        # increment k and start
        start += 1
        end += 1
    
    # return max items
    return new_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
