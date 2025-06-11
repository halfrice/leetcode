from spiral_matrix_ii import Solution

solution = Solution()


def test_case_1():
    n = 3
    expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert solution.generateMatrix(n) == expected


def test_case_2():
    n = 1
    expected = [[1]]
    assert solution.generateMatrix(n) == expected


def test_case_3():
    n = 4
    expected = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    assert solution.generateMatrix(n) == expected
