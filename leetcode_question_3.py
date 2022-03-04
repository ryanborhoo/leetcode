from collections import Counter
from collections import defaultdict


# [3] https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0
    while end < len(s):
        # print(s[end])
        # print(counter[s[end]])
        counter[s[end]] += 1
        if counter[s[end]] > 1:
            count += 1
        end += 1
        while count > 0:
            counter[s[start]] -= 1
            if counter[s[start]] > 0:
                count -= 1
            start += 1
        res = max(res, end-start)
    return res

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
print(lengthOfLongestSubstring(s))
