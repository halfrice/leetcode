# https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        def merge(intervals):
            intervals.sort()

            res = [intervals[0]]

            for start, end in intervals[1:]:
                if res[-1][1] < start:
                    res.append([start, end])
                else:
                    res[-1][1] = max(res[-1][1], end)

            return res

        intervals.append(newInterval)

        return merge(intervals)
