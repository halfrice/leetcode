# https://leetcode.com/problems/majority-element/description/


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # https://en.wikipedia.org/wiki/Boyer-Moore_majority_vote_algorithm
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res
