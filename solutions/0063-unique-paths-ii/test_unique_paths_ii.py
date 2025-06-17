from unique_paths_ii import Solution

solution = Solution()


def test_case_1():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected = 2
    assert solution.uniquePathsWithObstacles(obstacleGrid) == expected


def test_case_2():
    obstacleGrid = [[0, 1], [0, 0]]
    expected = 1
    assert solution.uniquePathsWithObstacles(obstacleGrid) == expected
