from find_n_unique_integers_sum_up_to_zero import Solution

solution = Solution()


def test_case_1():
    n = 5
    result = solution.sumZero(n)
    expected = 0
    assert sum(result) == expected


def test_case_2():
    n = 3
    result = solution.sumZero(n)
    expected = 0
    assert sum(result) == expected


def test_case_3():
    n = 1
    result = solution.sumZero(n)
    expected = 0
    assert sum(result) == expected
