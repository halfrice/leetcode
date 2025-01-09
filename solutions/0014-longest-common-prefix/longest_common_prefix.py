# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        s1 = strs[0]

        for i in range(len(s1)):
            for s in strs:
                if i == len(s) or s[i] != s1[i]:
                    return res
            res += s1[i]

        return res
