# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        def swap(x, y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp

        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1
