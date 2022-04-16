from collections import Counter
from collections import defaultdict


# [26] https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once. The relative order of the elements should be kept the same.

def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [0, 1, 2]
print(removeDuplicates(nums))
