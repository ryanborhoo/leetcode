from collections import Counter
from collections import defaultdict


# [209] https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

def minSubArrayLen(target, nums):
    if not nums:
        return 0
    start = 0
    end = 0
    total = 0
    res = float('inf')
    while end < len(nums):
        total = total + nums[end]
        while total >= target:
            res = min(end - start + 1, res)
            total = total - nums[start]
            start += 1
        end += 1
    return res if res != 'inf' else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
