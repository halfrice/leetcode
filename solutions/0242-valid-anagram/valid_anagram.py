# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for c in t:
            if c not in hashmap:
                return False
            else:
                hashmap[c] -= 1

        for v in hashmap.values():
            if v > 0 or v < 0:
                return False
        return True
