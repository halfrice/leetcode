# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
