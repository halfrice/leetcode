from equal_row_and_column_pairs import Solution

solution = Solution()


def test_case_1():
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    expected = 1
    assert solution.equalPairs(grid) == expected


def test_case_2():
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    expected = 3
    assert solution.equalPairs(grid) == expected


def test_case_3():
    grid = [[13, 13], [13, 13]]
    expected = 4
    assert solution.equalPairs(grid) == expected
