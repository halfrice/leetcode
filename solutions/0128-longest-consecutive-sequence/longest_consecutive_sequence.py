# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        history = {}
        longest = 0

        for n in nums:
            left = history.get(n - 1, 0)
            right = history.get(n + 1, 0)
            count = left + 1 + right
            history[n - left] = count
            history[n + right] = count
            longest = max(longest, count)

        return longest
