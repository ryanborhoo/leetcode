import bisect
from collections import defaultdict


# [1889] https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# You have n packages that you are trying to place in boxes, one package in each box.
# There are m suppliers that each produce boxes of different sizes (with infinite supply).
# A package can be placed in a box if the size of the package is less than or equal to the size of the box.


def minWastedSpace(packages, boxes):
    mod = 10 ** 9 + 7
    packages.sort()  # [2,3,5]
    ans = float("inf")  # infinite large value
    for box in boxes:  # [[4, 8], [2, 8]]
        box.sort()  # [4, 8]
        if packages[-1] > box[-1]:
            continue
        idx = 0
        curr = 0
        for b in box:
            # print(b) # 4,8   # 2,8
            last = idx
            idx = bisect.bisect_right(packages, b)
            # print(idx)  # 2,3  # 1,3
            # print(last) # 0,2  # 0,1
            curr += (idx - last) * b
            # print(curr)  # 8, 8+8  #2, 2+16
        ans = min(ans, curr)  # 16
        # sum(sum(packages)) = 10
    return (ans-sum(packages)) % mod if ans != float('inf') else -1


packages = [2, 3, 5]
boxes = [[4, 8], [2, 8]]
print(minWastedSpace(packages, boxes))
