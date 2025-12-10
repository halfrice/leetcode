from transpose_matrix import Solution

solution = Solution()


def test_case_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert solution.transpose(matrix) == expected


def test_case_2():
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert solution.transpose(matrix) == expected
