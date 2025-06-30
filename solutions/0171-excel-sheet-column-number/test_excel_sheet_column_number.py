from excel_sheet_column_number import Solution

solution = Solution()


def test_case_1():
    columnTitle = 'A'
    expected = 1
    assert solution.titleToNumber(columnTitle) == expected


def test_case_2():
    columnTitle = 'AB'
    expected = 28
    assert solution.titleToNumber(columnTitle) == expected


def test_case_3():
    columnTitle = 'ZY'
    expected = 701
    assert solution.titleToNumber(columnTitle) == expected


def test_case_4():
    columnTitle = 'YZ'
    expected = 676
    assert solution.titleToNumber(columnTitle) == expected


def test_case_5():
    columnTitle = 'FXSHRXW'
    expected = 2147483647
    assert solution.titleToNumber(columnTitle) == expected
