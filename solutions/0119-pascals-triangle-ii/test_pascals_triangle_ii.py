from pascals_triangle_ii import Solution

solution = Solution()


def test_case_1():
    rowIndex = 3
    expected = [1, 3, 3, 1]
    assert solution.getRow(rowIndex) == expected


def test_case_2():
    rowIndex = 0
    expected = [1]
    assert solution.getRow(rowIndex) == expected


def test_case_3():
    rowIndex = 1
    expected = [1, 1]
    assert solution.getRow(rowIndex) == expected
