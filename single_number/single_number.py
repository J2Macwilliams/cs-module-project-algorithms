'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
Understanding:
- List of integers
- There will be more than one integer
- Single integer is what we are looking for
- Just trying to get a solution down
'''
import time

start_time = time.time()

def single_number(arr):
    # Plan
    # count similar elements in list
    # filter singular item out
    # map filtered item to new list
    new_arr = [x for x in arr if arr.count(x) < 2] # O(n)
    # return new list item
    return new_arr[0]

single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0])
end_time = time.time()

# First Pass
# runtime: 2.3126602172851562e-05 seconds
# Runtime Complexity: O(n), only has to map & filter out a single item, but could be a very long list.


print(f"runtime: {end_time - start_time} seconds")

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")