# [35] https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# Time: O(logn) Space:O(1)
# Here we'll do a basic binary search operation to find the target value and then return that index
# if we didn't get the index, then we can just return the start pointer
# as it'll be in the exact location where the target value should be placed

def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1  # 3
    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


nums = [1, 3, 5, 6]
# target = 5
# target = 2
target = 7

print(searchInsert(nums, target))
