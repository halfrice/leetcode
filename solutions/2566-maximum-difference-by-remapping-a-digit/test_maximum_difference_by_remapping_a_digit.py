from maximum_difference_by_remapping_a_digit import Solution

solution = Solution()


def test_case_1():
    num = 11891
    expected = 99009
    assert solution.minMaxDifference(num) == expected


def test_case_2():
    num = 90
    expected = 99
    assert solution.minMaxDifference(num) == expected
