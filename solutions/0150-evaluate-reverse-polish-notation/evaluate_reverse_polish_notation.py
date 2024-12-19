# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }
        stack = []

        for t in tokens:
            if t not in op:
                stack.append(int(t))
            elif t in op and len(stack) >= 2:
                y = stack.pop()
                x = stack.pop()
                res = op[t](x, y)
                stack.append(res)

        return stack[0] if len(stack) == 1 else None
