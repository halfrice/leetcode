# https://leetcode.com/problems/candy/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        res = [1] * len(ratings)

        # Traverse through array from left to right. Any child that has a higher
        # rating than it's left-hand neighbor gets 1 more candy
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                res[i] = res[i - 1] + 1

        # Traverse from right to left. Compare child with right-hand neighbor and only
        # adjust candy amount from the first pass if adding 1 to right-hand neighbor is
        # more than the amount the child is currently allocated
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)
