'''
Input: a List of integers
Returns: a List of integers
'''
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
    for i in range(0, len(arr)):
        my_args = [x for x in arr]
        my_args.pop(i)
        # append to value to new array 
        new_array.append(my_product(*my_args))
        my_args.insert(i, arr[i])
    # return new_array
    return new_array


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
