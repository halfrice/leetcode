# https://leetcode.com/problems/spiral-matrix-ii/


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        m = [[0] * n for _ in range(n)]  # matrix
        # Direction of movement in order to achieve spiral: right, down, left, and up
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # Starting position
        x, y = 0, 0
        # Starting direction (right)
        d = 0

        # Iterate from 1 to n**2
        for i in range(1, n * n + 1):
            # Insert iterator value to the matrix
            m[x][y] = i
            # Look ahead and calculate the next position
            nx = x + dirs[d][0]  # next x
            ny = y + dirs[d][1]  # next y

            # Check if the next position is out of bounds or already filled
            if nx < 0 or ny < 0 or nx >= n or ny >= n or m[nx][ny]:
                # Change direction
                d = (d + 1) % 4
                # Recalulate the next position
                nx = x + dirs[d][0]
                ny = y + dirs[d][1]

            # Move to the next position
            x, y = nx, ny

        return m
