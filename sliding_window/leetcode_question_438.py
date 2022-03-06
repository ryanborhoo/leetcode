from collections import Counter
from collections import defaultdict


# [438] https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    counter = Counter(p)
    start, end = 0, 0
    count = len(p)
    res = []
    # print(count)  # 3
    while end < len(s):
        # only update counter when match char in p
        # print(counter[s[end]])  # 1,1,1,0,1,1,0,0,1,0
        counter[s[end]] -= 1
        # print(counter[s[end]])  # 0,0,0,-1,0,0,-1,-1,0,-1
        if counter[s[end]] >= 0:
            print(count)
            count -= 1
            # print(count)
        end += 1

        if count == 0:
            res.append(start)

        # not use a while, because restrict the length
        if end - start == len(p):
            counter[s[start]] += 1
            # exclude char not in p, because always negative
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return res


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))
