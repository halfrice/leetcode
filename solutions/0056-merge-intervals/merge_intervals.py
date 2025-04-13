# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
