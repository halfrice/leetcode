# https://leetcode.com/problems/valid-sudoku/

import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sects = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                n = board[row][col]
                if n == '.':
                    continue
                elif (
                    n in rows[row] or n in cols[col] or n in sects[(row // 3, col // 3)]
                ):
                    return False
                else:
                    rows[row].add(n)
                    cols[col].add(n)
                    sects[(row // 3, col // 3)].add(n)
        return True
