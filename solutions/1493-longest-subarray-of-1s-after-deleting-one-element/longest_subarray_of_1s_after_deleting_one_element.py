# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Two lists: one forwards pass, and backwards pass. Store consecutive ones
        # (to the left or right) at the current index
        len_nums = len(nums)
        left = [0] * len_nums
        right = [0] * len_nums

        # Populate left list with consecutive ones to the left of index
        for i in range(1, len_nums):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1

        # Populate the right list with consecutive ones to the left of index
        for i in range(len_nums - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1

        return max(x + y for x, y in zip(left, right))
