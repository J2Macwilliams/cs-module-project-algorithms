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
    # if cookie is 1: only one way to eat them
    if n < 2:
        return 1
    # if cookies are 2: there are 2 ays to eat them
    if n == 2:
        return 2
    # if cookies are 3: there are 4 ways to eat them
    if n == 3 :
        return 4
    # # create recursive call
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
