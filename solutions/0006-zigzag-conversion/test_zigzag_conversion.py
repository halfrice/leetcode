from zigzag_conversion import Solution

solution = Solution()


def test_case_1():
    s = 'PAYPALISHIRING'
    num_rows = 3
    expected = 'PAHNAPLSIIGYIR'
    assert solution.convert(s, num_rows) == expected


def test_case_2():
    s = 'PAYPALISHIRING'
    num_rows = 4
    expected = 'PINALSIGYAHRPI'
    assert solution.convert(s, num_rows) == expected


def test_case_3():
    s = 'A'
    num_rows = 1
    expected = 'A'
    assert solution.convert(s, num_rows) == expected


def test_custom_case_1():
    s = 'PAYPALISHIRINGABCDEFG'
    num_rows = 5
    expected = 'PHCASIBDYIRAEPLIGFANG'
    assert solution.convert(s, num_rows) == expected


def test_custom_case_2():
    s = 'ABCD'
    num_rows = 3
    expected = 'ABDC'
    assert solution.convert(s, num_rows) == expected
