# https://leetcode.com/problems/valid-mountain-array/


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        # Ascend from left side to first peak seen
        i = 0
        while i < len(arr) - 2 and arr[i] < arr[i + 1]:
            i += 1

        # Ascend from right
        j = len(arr) - 1
        while j > 1 and arr[j - 1] > arr[j]:
            j -= 1

        # If both pointers are equal then it's a valid mountain array
        return i == j
