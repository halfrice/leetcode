# https://leetcode.com/problems/equal-row-and-column-pairs/


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        grid2 = [list(c) for c in zip(*grid)]
        pairs = 0

        for r in grid:
            for c in grid2:
                if r == c:
                    pairs += 1

        return pairs
