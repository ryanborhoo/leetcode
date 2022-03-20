from math import ceil


# [875] https://leetcode.com/problems/koko-eating-bananas/
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.


class Solution:
    def minEatingSpeed(self, piles, h):
        def can_eat(k):
            time = 0
            for pile in piles:
                time += ceil(pile / k)
            return time <= h

        left = 1
        right = max(piles)  # 11
        while left <= right:
            mid = left + (right - left) // 2
            if can_eat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# class Solution:
#     def minEatingSpeed(self, piles, h):
#         beg, end = 0, max(piles)
#         while beg + 1 < end:
#             mid = (beg + end) // 2
#             if sum(ceil(i / mid) for i in piles) > h:
#                 beg = mid
#             else:
#                 end = mid
#         return end


piles = [3, 6, 7, 11]
h = 8

# piles = [30, 11, 23, 4, 20]
# h = 5

# piles = [30, 11, 23, 4, 20]
# h = 6
solution = Solution()
print(solution.minEatingSpeed(piles, h))
