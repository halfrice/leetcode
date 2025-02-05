# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # In-place solution
        # Use the first row and col to mark what needs to be zeroed out later
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero_flag = False

        # Mark which rows and cols will need to be set to zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero_flag = True

        # Zero out matrix based on first row and col markings
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Then zero out rows if the first column is set to zero
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Then zero out cols if the first row is set to zero
        if row_zero_flag:
            for c in range(cols):
                matrix[0][c] = 0
