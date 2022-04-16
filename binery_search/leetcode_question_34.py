# [34] https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.

def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return [-1, -1]
    for i in range(mid, len(nums)):
        if nums[i] != target:
            high = i - 1
            break
    for i in range(mid, -1, -1):
        if nums[i] != target:
            low = i + 1
            break
    return [high, low]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
