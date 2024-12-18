from string_to_integer import Solution

solution = Solution()


def test_case_1():
    s = '42'
    expected = 42
    assert solution.myAtoi(s) == expected


def test_case_2():
    s = '-042'
    expected = -42
    assert solution.myAtoi(s) == expected


def test_case_3():
    s = '1337c0d3'
    expected = 1337
    assert solution.myAtoi(s) == expected


def test_case_4():
    s = '0-1'
    expected = 0
    assert solution.myAtoi(s) == expected


def test_case_5():
    s = ''
    expected = 0
    assert solution.myAtoi(s) == expected


def test_case_6():
    s = ' '
    expected = 0
    assert solution.myAtoi(s) == expected


def test_custom_case_1():
    s = '   -00700'
    expected = -700
    assert solution.myAtoi(s) == expected
