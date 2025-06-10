# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            ai = int(a[i]) if i >= 0 else 0
            bi = int(b[j]) if j >= 0 else 0
            carry += ai + bi
            carry, digit = divmod(carry, 2)
            res.append(str(digit))
            i -= 1
            j -= 1

        return ''.join(res[::-1])
