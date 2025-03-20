# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i, j = -1, -1

        while j < len(nums) - 1:
            j += 1

            if nums[j] == 0:
                k -= 1

            if k < 0:
                i += 1

                if nums[i] == 0:
                    k += 1

        return j - i
