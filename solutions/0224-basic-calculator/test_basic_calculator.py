from basic_calculator import Solution

solution = Solution()


def test_case_1():
    s = '1 + 1'
    expected = 2
    assert solution.calculate(s) == expected


def test_case_2():
    s = ' 2-1 + 2 '
    expected = 3
    assert solution.calculate(s) == expected


def test_case_3():
    s = '(1+(4+5+2)-3)+(6+8)'
    expected = 23
    assert solution.calculate(s) == expected
