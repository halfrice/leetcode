from pascals_triangle import Solution

solution = Solution()


def test_case_1():
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert solution.generate(numRows) == expected


def test_case_2():
    numRows = 1
    expected = [[1]]
    assert solution.generate(numRows) == expected
