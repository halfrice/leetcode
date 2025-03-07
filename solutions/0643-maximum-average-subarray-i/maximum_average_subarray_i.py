# https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Set the initial sum and max average of the first k elements
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_average = sum / k

        # Update sum and max_average for the remaining elements
        for i in range(k, len(nums)):
            sum -= nums[i - k]
            sum += nums[i]
            max_average = max(sum / k, max_average)

        return max_average
