# https://leetcode.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        z = m + n - 1

        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[z] = nums1[m - 1]
                m -= 1
            else:
                nums1[z] = nums2[n - 1]
                n -= 1
            z -= 1
