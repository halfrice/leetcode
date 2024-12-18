# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # Strip whitespace
        s = s.lstrip()

        # Determine sign
        is_negative = False
        i = 0
        s_len = len(s)
        if i < s_len and s[i] == '-':
            is_negative = True
            i += 1
        elif i < s_len and s[i] == '+':
            i += 1

        # Read ints until first non-int is found
        r = ''
        while i < s_len and s[i].isdigit():
            r += s[i]
            i += 1
        if not r:
            return 0

        # Restore sign
        if is_negative:
            r = '-' + r

        # Cast string to int
        r = int(r)

        # Round ints that are out of 32-bit signed int bounds
        negative_limit = -(2**31)
        positive_limit = 2**31 - 1
        if r < negative_limit:
            return negative_limit
        elif r > positive_limit:
            return positive_limit
        return r
