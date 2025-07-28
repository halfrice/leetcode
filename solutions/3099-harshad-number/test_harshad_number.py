from harshad_number import Solution

solution = Solution()


def test_case_1():
    x = 18
    expected = 9
    assert solution.sumOfTheDigitsOfHarshadNumber(x) == expected


def test_case_2():
    x = 23
    expected = -1
    assert solution.sumOfTheDigitsOfHarshadNumber(x) == expected
