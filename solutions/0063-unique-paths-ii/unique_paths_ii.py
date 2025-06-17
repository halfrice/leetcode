# https://leetcode.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        len_x, len_y = len(obstacleGrid[0]), len(obstacleGrid)
        res = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        # Hardcode starting cell
        if obstacleGrid[0][0] == 0:
            res[0][0] = 1

        # Process first column
        for y in range(1, len_y):
            # Check for obstacle at current position
            if obstacleGrid[y][0] == 0:
                # Set the value at cur pos to the previous pos
                res[y][0] = res[y - 1][0]

        # Process first row
        for x in range(1, len_x):
            if obstacleGrid[0][x] == 0:
                res[0][x] = res[0][x - 1]

        # Process remaining cells
        for y in range(1, len_y):
            for x in range(1, len_x):
                if obstacleGrid[y][x] == 0:
                    res[y][x] = res[y][x - 1] + res[y - 1][x]

        return res[-1][-1]
