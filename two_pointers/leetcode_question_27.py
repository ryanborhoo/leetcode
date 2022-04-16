# [27] https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

def removeElement(nums, val):
    slow = 0
    for fast in range(0, len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
