# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        # Mod k by length of array for wrap-around cases
        k = k % len(nums)

        # Reverse values in nums array
        reverse(0, len(nums) - 1)

        # Reverse up to k
        reverse(0, k - 1)

        # Reverse from k and after
        reverse(k, len(nums) - 1)
