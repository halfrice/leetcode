# https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Set i to the second to last index of nums
        i = len(nums) - 2

        # Decrement i until nums[i] is less than nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If i is a valid index
        if i >= 0:
            # Set j to the last index of nums
            j = len(nums) - 1

            # Decrement j until nums[j] is greater than nums[i]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] with nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse everything after nums[i]
        nums[i + 1 :] = nums[i + 1 :][::-1]
