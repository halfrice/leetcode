# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = 1
        res = 0
        len_s = len(s)
        i = 0

        while i < len_s:
            c = s[i]

            if c.isdigit():
                # Create int from string of num
                n = 0

                while i < len_s and s[i].isdigit():
                    n = n * 10 + int(s[i])
                    i += 1

                res += op * n
                i -= 1
            elif c == '+':
                op = 1
            elif c == '-':
                op = -1
            elif c == '(':
                # Save progress to the stack and reset res and op
                stack.append(res)
                stack.append(op)
                res = 0
                op = 1
            elif c == ')':
                # Handle the result inside parens
                res *= stack.pop()  # Pop the saved operator and apply to result
                res += stack.pop()  # Pop the saved number and add it to result

            i += 1

        return res
