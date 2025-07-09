# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        arrow_pos = float('-inf')
        arrows_used = 0

        # Iterate through a sorted-by-end-values points list
        for start, end in sorted(points, key=lambda p: p[1]):
            # The arrow fired is left of the current ballon
            if arrow_pos < start:
                # Another arrow must be fired
                arrows_used += 1
                # Update prev arrows position to the end of the current ballon
                # This skip-ahead works because the points array is sorted by end vals
                arrow_pos = end

        return arrows_used
