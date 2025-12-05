# leetcode.com/problems/monotonic-array/

from itertools import pairwise


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        ascending = all(a <= b for a, b in pairwise(nums))
        descending = all(a >= b for a, b in pairwise(nums))

        return ascending or descending

    # def isMonotonic(self, nums: list[int]) -> bool:
    #     i = 0
    #     while i + 1 < len(nums) and nums[i] <= nums[i + 1]:
    #         i += 1
    #     ascending = True if i == len(nums) - 1 else False
    #
    #     i = 0
    #     while i + 1 < len(nums) and nums[i] >= nums[i + 1]:
    #         i += 1
    #     descending = True if i == len(nums) - 1 else False
    #
    #     return ascending or descending
