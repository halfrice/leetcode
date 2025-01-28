# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Sliding window solution
        total = 0
        res = float('inf')
        i = 0

        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                res = min(j - i + 1, res)
                total -= nums[i]
                i += 1

        return 0 if res == float('inf') else res
