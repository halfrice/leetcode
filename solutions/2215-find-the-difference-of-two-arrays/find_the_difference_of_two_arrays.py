# https://leetcode.com/problems/find-the-difference-of-two-arrays/


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1s = set(nums1)
        n2s = set(nums2)

        n1a = list(n1s - n2s)
        n2a = list(n2s - n1s)

        return [n1a, n2a]
