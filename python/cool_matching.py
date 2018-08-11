'''
challenge question

Joe has 2n points on a circle. We are looking for the number of matching that are "cool". A cool matching is a matching of all points such that no two matches are crossing each other. For example if we have 4 points on a circle the matching (1,3)(2,4) is not cool since (1,3) intersects with (2,4). In this case the matching (1,2)(3,4) and (1,4)(2,3) are the only cool matching. If we have 6 points we get 5 "cool" matchings: 
(1,2)(3,4)(5,6)
(2,3)(4,5)(6,1)
(1,4)(2,3)(5,6)
(1,2)(3,6)(4,5)
(1,6)(2,5)(3,4)
Write a function that for a given n will return the number of cool matchings of 2n points.

test cases

Input -› {"n": 1}
Expected output -› 1
Input -› {"n": 2}
Expected output -› 2
'''
from functools import wraps
def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def answer(n):
    result = 0
    if n == 1 or n == 0: return 1
    for i in range(n):
        result += answer(n-i-1) * answer(i)
    return result

def main():
    for i in range(6):
        print(i, answer(i))

if __name__ == '__main__':
    main()