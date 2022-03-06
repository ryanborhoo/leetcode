from collections import Counter
from collections import defaultdict
# [76] https://leetcode.com/problems/minimum-window-substring/
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T

def minWindow(s, t):
    counter = Counter(t)
    start, end = 0, 0
    count = len(t)
    res = [float('inf'), 0]
    # print(count)  # 3
    while end < len(s):
        # print(counter[s[end]])  # 1,0,0,1,0,1,-1,-1,-1,0,1,0,1
        counter[s[end]] -= 1
        # print(counter[s[end]])  # 0,-1,-1,0,-1,0,-2,-2,-2,-1,0,-1,0
        # consider duplicate char in t
        if counter[s[end]] >= 0:
            # print(count)  # 3,2,1,1,1
            count -= 1
            # print(count)  # 2,1,0,0,0
        # print(end)  # 0 => 12
        end += 1
        # print(end)  # 1 => 13
        # print(count)  # 2,2,2,1,1,0,1,1,1,1,0,1,0
        while count == 0:
            # print(count)  # 10 0s
            # update minimum here, inner while loop
            if end - start < res[0]:
                # print(res)  # [inf, 0]
                res = (end - start, start)
                # print(res)  # (6,0) (6,0) (5,8) (5,8) (4,9)
            # print(counter[s[start]])  # 0,-2,-2,-1,-2,0,-1,-1,-1,0
            counter[s[start]] += 1
            # print(counter[s[start]])  # 1,-1,-1,0,-1,1,0,0,0,1
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return s[res[1]:res[0] + res[1]] if res[0] != float('inf') else ''


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))


