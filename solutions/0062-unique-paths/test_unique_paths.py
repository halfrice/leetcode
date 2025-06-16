from unique_paths import Solution

solution = Solution()


def test_case_1():
    m = 3
    n = 7
    expected = 28
    assert solution.uniquePaths(m, n) == expected


def test_case_2():
    m = 3
    n = 2
    expected = 3
    assert solution.uniquePaths(m, n) == expected
