# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            # Add chars to stack until we reach a ]
            if s[i] != ']':
                stack.append(s[i])
            else:
                # After a ] is encountered, walk backwards until we find [
                # while creating a substring (t) along the way
                t = ''
                while stack[-1] != '[':
                    t = stack.pop() + t
                # Pop the [ from stack
                stack.pop()

                # Create a string of the number to the left of [ if it exists
                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                # Convert the string to int and multiply the substring
                stack.append(int(n) * t)

        return ''.join(stack)
