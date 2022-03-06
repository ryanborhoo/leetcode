from collections import Counter
from collections import defaultdict

# [3] https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    counter = defaultdict(int)
    start, end = 0, 0
    count = 0
    res = 0
    while end < len(s):
        # print(s[end])
        # print(counter[s[end]]) # 0,0,0,1,1,1,1,1
        counter[s[end]] += 1
        # print(counter[s[end]]) # 1,1,1,2,2,2,2,2
        if counter[s[end]] > 1:
            # print(count)  # 0,0,0,0,0
            count += 1
            # print(count)  # 1,1,1,1,1
        end += 1
        # print (count)  # 0,0,0,1,1,1,1,1
        while count > 0:
            # print(counter[s[start]])  # 2,2,2,1,2,1,2
            counter[s[start]] -= 1
            # print(counter[s[start]])   # 1,1,1,0,1,0,1
            if counter[s[start]] > 0:
                count -= 1
            start += 1
        # print(end)  # 1,2,3,4,5,6,7,8
        # print(start) # 0,0,0,1,2,3,5,7
        res = max(res, end-start)
    return res

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
print(lengthOfLongestSubstring(s))
