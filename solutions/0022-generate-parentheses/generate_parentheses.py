# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append(''.join(stack))
                return

            if opened < n:
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(')')
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res

    # An easier to understand solution, though less efficient
    # def generateParenthesis(self, n: int) -> list[str]:
    #     res = []
    #
    #     def travel(left: int, right: int, s: str):
    #         if len(s) == n * 2:
    #             res.append(s)
    #             return
    #
    #         if left < n:
    #             travel(left + 1, right, s + '(')
    #
    #         if right < left:
    #             travel(left, right + 1, s + ')')
    #
    #     travel(0, 0, '')
    #     return res
