# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        seen = set()

        for n in nums:
            if n in seen:
                return n

            seen.add(n)
