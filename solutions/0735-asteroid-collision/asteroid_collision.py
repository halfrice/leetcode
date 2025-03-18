# https://leetcode.com/problems/asteroid-collision/


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                if stack and stack[-1] == -a:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)
            else:
                stack.append(a)

        return stack
