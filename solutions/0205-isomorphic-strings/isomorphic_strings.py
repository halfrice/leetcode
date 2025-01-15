# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash, thash = {}, {}
        for i in range(len(s)):
            if (s[i] in shash and shash[s[i]] != t[i]) or (
                t[i] in thash and thash[t[i]] != s[i]
            ):
                return False
            shash[s[i]] = t[i]
            thash[t[i]] = s[i]
        return True
