# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, si = stack.pop()
                res[si] = i - si
            stack.append([t, i])

        return res
