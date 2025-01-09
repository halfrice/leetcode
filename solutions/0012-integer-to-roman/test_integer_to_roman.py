from integer_to_roman import Solution

solution = Solution()


def test_case_1():
    num = 3749
    expected = 'MMMDCCXLIX'
    assert solution.intToRoman(num) == expected


def test_case_2():
    num = 58
    expected = 'LVIII'
    assert solution.intToRoman(num) == expected


def test_case_3():
    num = 1994
    expected = 'MCMXCIV'
    assert solution.intToRoman(num) == expected
