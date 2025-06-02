# https://leetcode.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def backtrack(r):
            # When row equals size n, all Queens are valid and a result is found
            if r == n:
                res.append([''.join(x) for x in board])
                return

            for c in range(n):
                # Check if placing a Queen can be done without being spawn killed
                if not col[c] and not diag[r + c] and not neg_diag[n - r + c]:
                    # Add the Queens position to the board and positional lists
                    col[c] = diag[r + c] = neg_diag[n - r + c] = True
                    board[r][c] = 'Q'

                    backtrack(r + 1)

                    # Remove the Queens position to the board and lists
                    col[c] = diag[r + c] = neg_diag[n - r + c] = False
                    board[r][c] = '.'

        board = [['.'] * n for _ in range(n)]
        col = [False] * n
        diag = [False] * (n * 2)
        neg_diag = [False] * (n * 2)
        res = []

        backtrack(0)

        return res
