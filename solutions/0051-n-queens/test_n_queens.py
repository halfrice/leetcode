from n_queens import Solution

solution = Solution()


def test_case_1():
    n = 4
    expected = [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
    assert solution.solveNQueens(n) == expected


# def test_case_2():
#     n = 1
#     expected = [['Q']]
#     assert solution.solveNQueens(n) == expected
