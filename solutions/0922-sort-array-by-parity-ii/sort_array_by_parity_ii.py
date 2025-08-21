# https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        j = 1  # j represents odd indexes

        # i represents even indexes
        for i in range(0, len(nums), 2):
            # If an odd number exists where an even should be
            if nums[i] % 2 == 1:
                # Iterate through odd indexes until an even number is found
                while nums[j] % 2 == 1:
                    j += 2

                # Swap em
                nums[i], nums[j] = nums[j], nums[i]

        return nums
