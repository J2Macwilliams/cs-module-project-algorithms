'''
Input: an integer
Returns: an integer
'''
# Import time to calculate efficiency of code
import time

# establish start time
start_time = time.time()

def eating_cookies(n, cache=None):
    # Plan naive
    # there are only a limited amount of cookies
    # problem looks similar to fibonacci
    # except with three options
    # try Tribonacci sequence
    # set up base case
    if n < 0:
        return 0
    # if cookie is 1: only one way to eat them
    if n == 0:
        return 1
    # check if cached item
    if cache is not None and cache[n] > 0:
        return cache[n]
    # # create recursive call
    else:
        # for initializing cache for the first time
        if cache is None:
            # set cache up for cookie jar size
            cache = [0 for i in range(n + 1)]
            
        # store the value for the recursive call expressions in the cache at the index
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]

## First pass Solution times:
# eating_cookies(10) # runtime: 3.0994415283203125e-05 seconds
# eating_cookies(30) #runtime: 5.754578113555908 seconds

## Better Solutions with cache
# eating_cookies(10) # runtime: 0.00013184547424316406 seconds
# eating_cookies(30) # runtime: 0.00031375885009765625 seconds

end_time = time.time()

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

print(f"runtime: {end_time - start_time} seconds")