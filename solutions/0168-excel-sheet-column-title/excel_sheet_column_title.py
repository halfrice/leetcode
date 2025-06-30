# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber:
            columnNumber -= 1
            res.append(chr(65 + columnNumber % 26))
            columnNumber //= 26

        return ''.join(res[::-1])
