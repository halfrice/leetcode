# https://leetcode.com/problems/peak-index-in-a-mountain-array/


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # left = 1
        # right = len(arr) - 2
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            # The peak is in the left half
            if arr[mid] > arr[mid + 1]:
                right = mid
            # The peak is in the right half
            else:
                left = mid + 1

        return left
