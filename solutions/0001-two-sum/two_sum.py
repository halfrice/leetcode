# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for i, n in enumerate(nums):
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
