# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        li = bisect_left(nums, target)
        ri = bisect_left(nums, target + 1)

        if li == ri:
            return [-1, -1]

        return [li, ri - 1]
