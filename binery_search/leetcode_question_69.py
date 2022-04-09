# [69] https://leetcode.com/problems/sqrtx/
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

def mySqrt(x):
    low = 0
    high = x + 1
    while low < high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid
    return low - 1


x = 8
print(mySqrt(x))
