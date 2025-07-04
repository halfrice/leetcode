# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Exclusive or solution
        res = 0

        for n in nums:
            res ^= n

        return res
