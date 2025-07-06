# https://leetcode.com/problems/game-of-life/


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for x in range(rows):
            for y in range(cols):
                neighbors = -(board[x][y])

                # xs is x-small, the smaller x, the inner x, the child x
                # Iterate through the sub-matrix: 3x3 grid with board[x][y] as its center
                for xs in range(x - 1, x + 2):
                    for ys in range(y - 1, y + 2):
                        # Check neighbors pulse and if in bounds
                        if 0 <= xs < rows and 0 <= ys < cols and board[xs][ys] > 0:
                            # Increase neighbor count if alive
                            neighbors += 1

                # Any live cell with fewer than two live neighbors dies
                # Any live cell with more than three live neighbors dies
                if board[x][y] and (neighbors < 2 or neighbors > 3):
                    # Marked for death
                    board[x][y] = 2

                # Any dead cell with exactly three live neighbors is reincarnated
                if not board[x][y] and neighbors == 3:
                    # About to be born
                    board[x][y] = -1

        # The Reaper comes
        for x in range(rows):
            for y in range(cols):
                # Take this mf soul
                if board[x][y] == 2:
                    board[x][y] = 0
                # See you soon kid
                if board[x][y] == -1:
                    board[x][y] = 1
