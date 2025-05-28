# https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        return [n for i, n in enumerate(nums) if i + 1 != n]
