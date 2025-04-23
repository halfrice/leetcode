# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 1

        for _ in range(n):
            prev, cur = cur, prev + cur

        return cur
