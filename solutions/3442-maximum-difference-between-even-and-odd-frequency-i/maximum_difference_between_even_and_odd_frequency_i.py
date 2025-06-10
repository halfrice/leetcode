# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        max_odd = 0
        min_even = float('inf')

        for v in freq.values():
            if v % 2:
                max_odd = max(v, max_odd)
            else:
                min_even = min(v, min_even)

        return max_odd - min_even
