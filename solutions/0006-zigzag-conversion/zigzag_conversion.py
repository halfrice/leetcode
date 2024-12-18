# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        matrix = [''] * numRows
        mi = 0
        increment = -1

        for c in s:
            matrix[mi] += c
            if mi == 0 or mi == numRows - 1:
                increment *= -1
            mi += increment

        return ''.join(matrix)

    # Version 2
    # TODO: Finish optimization

    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows <= 1:
    #         return s
    #
    #     col_width = numRows * 2 - 2
    #     r = ''
    #     i = 0
    #     row = 0
    #     while len(r) < len(s) and row < numRows:
    #         i = row
    #         while True:
    #             r += s[i]
    #             if row > 0 and row < numRows - 1:
    #                 zag = i + (((numRows - 1) - row) * 2)
    #                 if zag < len(s) - 1:
    #                     r += s[i + (((numRows - 1) - row) * 2)]
    #             i += col_width
    #
    #             if i > len(s) - 1:
    #                 row += 1
    #                 break
    #
    #     return r
