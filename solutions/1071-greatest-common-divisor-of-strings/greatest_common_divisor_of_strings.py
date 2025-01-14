# https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        len1 = len(str1)
        len2 = len(str2)

        def is_divisor(ln):
            if len1 % ln or len2 % ln:
                return False
            f1 = len1 // ln
            f2 = len2 // ln
            return str1[:ln] * f1 == str1 and str1[:ln] * f2 == str2

        for ln in range(min(len1, len2), 0, -1):
            if is_divisor(ln):
                return str1[:ln]
        return ''
