from maximum_difference_between_even_and_odd_frequency_i import Solution

solution = Solution()


def test_case_1():
    s = 'aaaaabbc'
    expected = 3
    assert solution.maxDifference(s) == expected


def test_case_2():
    s = 'abcabcab'
    expected = 1
    assert solution.maxDifference(s) == expected


def test_case_3():
    s = 'tzt'
    expected = -1
    assert solution.maxDifference(s) == expected


def test_case_4():
    s = 'xkxzkkk'
    expected = -1
    assert solution.maxDifference(s) == expected
