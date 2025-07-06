# https://leetcode.com/problems/find-peak-element/


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            m = (j + i) >> 1

            # If the value at mid is greater than the right, find the peak in left
            if nums[m] > nums[m + 1]:
                j = m
            # Find the peak in right
            else:
                i = m + 1

        # At this point, i has met with j, so either i or j will contain a peak index
        return i
