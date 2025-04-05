# https://leetcode.com/problems/h-index/


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Sort and loop solution
        citations.sort(reverse=True)

        h = 0
        # Increase h each iteration as long as there are enough citations per index
        while h < len(citations) and citations[h] >= h + 1:
            h += 1

        return h
