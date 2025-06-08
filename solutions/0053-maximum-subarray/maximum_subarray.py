# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = sum = nums[0]

        for n in nums[1:]:
            if sum < 0:
                sum = 0

            sum += n
            max_sum = max(sum, max_sum)

        return max_sum
