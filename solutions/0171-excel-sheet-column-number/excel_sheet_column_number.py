# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for c in columnTitle:
            res = res * 26 + (ord(c) - 64)

        return res
