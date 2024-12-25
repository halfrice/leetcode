from search_a_2d_matrix import Solution

solution = Solution()


def test_case_1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    expected = True
    assert solution.searchMatrix(matrix, target) == expected


# def test_case_2():
#     matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
#     target = 13
#     expected = False
#     assert solution.searchMatrix(matrix, target) == expected
