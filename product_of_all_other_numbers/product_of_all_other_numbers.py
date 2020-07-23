'''
Input: a List of integers
Returns: a List of integers
'''
import time

start_time = time.time()
def product_of_all_other_numbers(arr):
    # Plan
    # create a new_array
    new_array = []
    # create my_product fn to return args
    def my_product(*args):
        result = 1
        for x in args:
            result *= x
        return result
    # loop through give arr to get num
    for i in range(0, len(arr)): # O(n)
        my_item = arr.pop(i)
        # append to value to new array 
        new_array.append(my_product(*arr))
        arr.insert(i, my_item)
    # return new_array
    return new_array

end_time = time.time()
#First Pass
# runtime: 4.0531158447265625e-06 seconds
# Runtime complexity is O(n^2), as mapping to gain new list of args to use

# Better Solution
# runtime: 1.1920928955078125e-06 seconds
# Runtime Complexity: O(n) - realized I didn't need another array. 

product_of_all_other_numbers([7, 9, 1, 8, 6, 7, 8, 8, 7, 10])

print(f"runtime: {end_time - start_time} seconds")

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
