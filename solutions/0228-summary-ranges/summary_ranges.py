# https://leetcode.com/problems/summary-ranges/description/


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0

        while i < len(nums):
            n = nums[i]

            # Add one to the value at i, then compare it with the value at nums[i+1}
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            # If there was a range, add it to results
            if n != nums[i]:
                res.append(f'{n}->{nums[i]}')
            # Add single number to results
            else:
                res.append(f'{nums[i]}')

            i += 1

        return res
