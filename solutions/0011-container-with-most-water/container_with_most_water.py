# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            usable_height = min(height[left], height[right])
            area = usable_height * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area
