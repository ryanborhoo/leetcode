# [33] https://leetcode.com/problems/search-in-rotated-sorted-array/
# an array sorted in ascending order is rotated at some pivot unknown,
# given a target value to search. If found in the array return its index,
#
# variation with rotated sort
def search_in_rotated_sorted_array(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[low] < nums[mid]:
            if nums[low] < target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target < nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
target = 3
print(search_in_rotated_sorted_array(nums, target))
