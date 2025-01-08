from roman_to_integer import Solution

solution = Solution()


def test_case_1():
    s = 'III'
    expected = 3
    assert solution.romanToInt(s) == expected


def test_case_2():
    s = 'LVIII'
    expected = 58
    assert solution.romanToInt(s) == expected


def test_case_3():
    s = 'MCMXCIV'
    expected = 1994
    assert solution.romanToInt(s) == expected
