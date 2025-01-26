# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = ''

        for c in path + '/':
            if c == '/':
                if s == '..':
                    if stack:
                        stack.pop()
                elif s and s != '.':
                    stack.append(s)
                s = ''
            else:
                s += c

        return '/' + '/'.join(stack)
