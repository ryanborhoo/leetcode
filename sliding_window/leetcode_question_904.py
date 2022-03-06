from collections import Counter
from collections import defaultdict


# [904] https://leetcode.com/problems/fruit-into-baskets/
# You have two baskets, and each basket can carry any quantity of fruit,
# but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?


def totalFruit(fruits):
    counter = defaultdict(int)
    start, end = 0, 0
    count = 0
    res = 0

    while end < len(fruits):
        # print(counter[fruits[end]])  # 0,0,0,1
        counter[fruits[end]] += 1
        # print(counter[fruits[end]])  # 1,1,1,2
        if counter[fruits[end]] == 1:
            # print(count)  # 0,1,2
            count += 1
            # print(count)  # 1,2,3
        end += 1
        # print(count)  # 1,2,3,2
        while count > 2:
            # print(counter[fruits[start]])  # 1
            counter[fruits[start]] -= 1
            # print(counter[fruits[start]])  # 0
            if counter[fruits[start]] == 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res


fruits = [0, 1, 2, 2]
print(totalFruit(fruits))
