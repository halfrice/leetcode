from divide_two_integers import Solution

solution = Solution()


def test_case_1():
    dividend = 10
    divisor = 3
    expected = 3
    assert solution.divide(dividend, divisor) == expected


def test_case_2():
    dividend = 7
    divisor = -3
    expected = -2
    assert solution.divide(dividend, divisor) == expected


def test_case_3():
    dividend = -2147483648
    divisor = -1
    expected = 2147483647
    assert solution.divide(dividend, divisor) == expected
