# https://leetcode.com/problems/largest-number-at-least-twice-of-others/


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = second_largest = -1
        dominant_index = -1

        for i, n in enumerate(nums):
            if n > largest:
                second_largest, largest = largest, n
                dominant_index = i
            elif n > second_largest:
                second_largest = n

        return dominant_index if largest >= second_largest * 2 else -1
