# https://leetcode.com/problems/find-pivot-index/


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        isum = 0

        for i in range(len(nums)):
            jsum = total - nums[i] - isum
            if isum == jsum:
                return i
            isum += nums[i]

        return -1
