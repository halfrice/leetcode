from minimum_path_sum import Solution

solution = Solution()


def test_case_1():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected = 7
    assert solution.minPathSum(grid) == expected


def test_case_2():
    grid = [[1, 2, 3], [4, 5, 6]]
    expected = 12
    assert solution.minPathSum(grid) == expected
