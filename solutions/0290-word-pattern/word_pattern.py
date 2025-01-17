# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        cmap = {}  # chars hashmap
        wmap = {}  # words hashmap

        for c, w in zip(pattern, words):
            if c not in cmap:
                cmap[c] = w
            if w not in wmap:
                wmap[w] = c
            if cmap[c] != w or wmap[w] != c:
                return False
        return True
