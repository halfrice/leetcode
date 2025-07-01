# https://leetcode.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        len_x, len_y = len(grid[0]), len(grid)
        res = [[0] * len_x for _ in range(len_y)]

        # Hardcode starting cell
        res[0][0] = grid[0][0]

        # Process first row
        for x in range(1, len_x):
            res[0][x] = res[0][x - 1] + grid[0][x]

        # Process first column
        for y in range(1, len_y):
            res[y][0] = res[y - 1][0] + grid[y][0]

        # Process remaining cells
        for y in range(1, len_y):
            for x in range(1, len_x):
                res[y][x] = min(res[y - 1][x], res[y][x - 1]) + grid[y][x]

        return res[-1][-1]
