# [167] https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.

def twoSum(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low < high:
        total = numbers[low] + numbers[high]
        if total == target:
            return [low + 1, high + 1]
        elif total > target:
            high = high - 1
        else:
            low = low + 1
    return []


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
