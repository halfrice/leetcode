from set_matrix_zeroes import Solution

solution = Solution()


def test_case_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution.setZeroes(matrix)
    assert matrix == expected


def test_case_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    solution.setZeroes(matrix)
    assert matrix == expected
