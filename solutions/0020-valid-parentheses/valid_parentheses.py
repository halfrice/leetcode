# https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for c in s:
            if c in brackets_map:
                if stack and stack[-1] == brackets_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        return False
