# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max_diff = 0

        for i in range(len(nums)):
            max_diff = max(abs(nums[i - 1] - nums[i]), max_diff)

        return max_diff
