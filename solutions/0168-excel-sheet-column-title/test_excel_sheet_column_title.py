from excel_sheet_column_title import Solution

solution = Solution()


def test_case_1():
    columnNumber = 1
    expected = 'A'
    assert solution.convertToTitle(columnNumber) == expected


def test_case_2():
    columnNumber = 28
    expected = 'AB'
    assert solution.convertToTitle(columnNumber) == expected


def test_case_3():
    columnNumber = 701
    expected = 'ZY'
    assert solution.convertToTitle(columnNumber) == expected


def test_case_4():
    columnNumber = 676
    expected = 'YZ'
    assert solution.convertToTitle(columnNumber) == expected


def test_case_5():
    columnNumber = 2147483647
    expected = 'FXSHRXW'
    assert solution.convertToTitle(columnNumber) == expected
