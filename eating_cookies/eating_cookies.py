'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Plan naive
    
    # there are only a limited amount of cookies
    # problem looks similar to fibonacci
    # except with three options
    # try Tribonacci sequence
    # set up base case
    # if cookie is greater than amount of cookies:
    if n == 0:
        return 0
    # if cookie is equal to one
    elif n == 1:
        return 1
    # if cookie is equal to two
    elif n == 2:
        return 1
    # if cookie is equal to three
    elif n ==3:
        return 1
    # create recursive call
    else:
        eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
