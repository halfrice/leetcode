# https://leetcode.com/problems/ant-on-the-boundary/

from itertools import accumulate


class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        # Get the prefix sums of nums
        sums = accumulate(nums)

        return sum(s == 0 for s in sums)
