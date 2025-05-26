# https://leetcode.com/problems/sudoku-solver/


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # DFS backtracking solution
        def dfs(i: int):
            # i is an iterator that runs through the list: empty_cells
            # If i reaches the length of empty_cells, every cell has has been filled,
            # so set is_solved flat to True and exit
            if i == len(empty_cells):
                self.is_solved = True
                return

            # Set the coords of the current empty cell
            x, y = empty_cells[i]

            # Try all numbers 1 - 9 within the empty cell
            for n in range(9):
                if (
                    not x_used[x][n]
                    and not y_used[y][n]
                    and not b_used[x // 3][y // 3][n]
                ):
                    # Set the number as used within its respective row, col, and block
                    x_used[x][n] = y_used[y][n] = b_used[x // 3][y // 3][n] = True
                    # Update the board with the number
                    board[x][y] = str(n + 1)

                    dfs(i + 1)

                    # Undo and backtrack if no solution was found
                    x_used[x][n] = y_used[y][n] = b_used[x // 3][y // 3][n] = False

                if self.is_solved:
                    return

        self.is_solved = False

        # Set lists with boolean flags for each number used in:
        x_used = [[False] * 9 for _ in range(9)]  # Rows
        y_used = [[False] * 9 for _ in range(9)]  # Columns
        b_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # Blocks
        empty_cells = []

        # Process board to fill empty_cells list and set flags for numbers used
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    empty_cells.append((x, y))
                else:
                    # Convert the number at its coordinate to an int
                    # Subtract by 1 to match the lists zero-based indexing
                    n = int(board[x][y]) - 1

                    x_used[x][n] = True
                    y_used[y][n] = True
                    b_used[x // 3][y // 3][n] = True

        dfs(0)

    # def solveSudoku(self, board: list[list[str]]) -> None:
    #     # 'Simple' backtracking solution. As of 5/26/2025, this solution passes 6/7
    #     # testcases with the last failing due to Time Limit Exceeded.
    #     def is_valid(x, y, n):
    #         for i in range(9):
    #             if (
    #                 board[x][i] == n
    #                 or board[i][y] == n
    #                 or board[((x // 3) * 3) + i // 3][((y // 3) * 3) + i % 3] == n
    #             ):
    #                 return False
    #         return True
    #
    #     def solve():
    #         for x in range(9):
    #             for y in range(9):
    #                 if board[x][y] == '.':
    #                     for n in map(str, range(1, 10)):
    #                         if is_valid(x, y, n):
    #                             board[x][y] = n
    #                             if solve():
    #                                 return True
    #                             board[x][y] = '.'
    #                     return False
    #         return True
    #
    #     solve()
