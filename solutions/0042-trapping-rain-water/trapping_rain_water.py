# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        res = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]

        return res
