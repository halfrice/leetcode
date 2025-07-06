# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []

        # j index represents the right edge
        for j, height in enumerate(heights):
            # max_i stores the farthest left edge for the current height
            max_i = j

            while stack and stack[-1][1] > height:
                # i represents the current (possible max) left edge
                i, h = stack.pop()
                # Get the width
                w = j - i
                # Update max_area
                max_area = max(max_area, w * h)
                # Move max_i back to i since it's the new max left edge found
                max_i = i

            stack.append((max_i, height))

        # Leftover heights in stack have a right edge of the length of heights list
        for i, h in stack:
            w = len(heights) - i
            max_area = max(max_area, w * h)

        return max_area
