from n_queens_ii import Solution

solution = Solution()


def test_case_1():
    n = 4
    expected = 2
    assert solution.totalNQueens(n) == expected


def test_case_2():
    n = 1
    expected = 1
    assert solution.totalNQueens(n) == expected
