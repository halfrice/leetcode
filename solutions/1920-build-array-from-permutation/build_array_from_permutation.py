# https://leetcode.com/problems/build-array-from-permutation/


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[n] for n in nums]
