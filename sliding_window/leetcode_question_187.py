from collections import Counter
from collections import defaultdict


# [187] https://leetcode.com/problems/repeated-dna-sequences/
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule. You may return the answer in any order.

def findRepeatedDnaSequences(s):
    counter = defaultdict(int)
    count = 10
    res = []
    for i in range(len(s) - count + 1):
        counter[s[i:i + count]] += 1
        if counter[s[i:i + count]] == 2:
            res.append(s[i:i + count])
    return res


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))
