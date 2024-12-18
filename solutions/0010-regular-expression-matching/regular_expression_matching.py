# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[i, j]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            m = i < len(s) and (p[j] == '.' or s[i] == p[j])
            if j + 1 < len(p) and p[j + 1] == '*':
                cache[i, j] = dfs(i, j + 2) or (m and dfs(i + 1, j))
                return cache[i, j]

            if m:
                return dfs(i + 1, j + 1)
            return False

        return dfs(0, 0)
