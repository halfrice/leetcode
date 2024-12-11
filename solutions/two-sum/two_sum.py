# two_sum.py
# leetcode.com/problems/two-sum


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        history = {}
        for i, n in enumerate(nums):
            if target - n in history:
                return [history[target - n], i]
            history[n] = i
