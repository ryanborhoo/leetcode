import bisect


# [367] https://leetcode.com/problems/valid-perfect-square/
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# standard scenario


def is_perfect_square(num):
    low = 1
    high = num // 2  # 14 // 2 = 7
    while low <= high:  # 1 <= 7, 1 <= 3, 3<=3, end
        mid = low + (high - low) // 2  # 1+(6//2)=4, 1+(2//2) = 2, mid=3
        if mid * mid == num:
            return True
        elif mid * mid < num:
            low = mid + 1  # low=2+1=3, low=3+1=4
        else:
            high = mid - 1  # high=4-1=3
    return False


# num = 16
num = 14
print(is_perfect_square(num))
