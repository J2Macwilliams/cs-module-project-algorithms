'''
Input: a List of integers
Returns: a List of integers
- int above 0 order does not matter as long as its before 0
'''
def moving_zeroes(arr):
    # Plan
    # A: for loop 
    for item in arr:
        # establish index of item
        i = arr.index(item)
        if item is not 0:
            # pop item from list
            arr.pop(i)
            # insert it at first index
            arr.insert(0, item)
                 
    # return changed array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")