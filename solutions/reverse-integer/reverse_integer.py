# reverse_integer.py


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        is_negative = False
        if s[0] == '-':
            is_negative = True
            s = s[1:]

        r = s[::-1]
        if is_negative:
            r = '-' + r

        r = int(r)
        if r < -(2**31) or r > 2**31 - 1:
            return 0
        return r
