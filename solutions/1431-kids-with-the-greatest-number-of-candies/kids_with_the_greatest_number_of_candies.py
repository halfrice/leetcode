# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        res = []

        for n in candies:
            if n + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res
