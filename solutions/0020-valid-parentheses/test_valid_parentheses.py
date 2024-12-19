from valid_parentheses import Solution

solution = Solution()


def test_case_1():
    s = '()'
    expected = True
    assert solution.isValid(s) == expected


def test_case_2():
    s = '()[]{}'
    expected = True
    assert solution.isValid(s) == expected


def test_case_3():
    s = '(]'
    expected = False
    assert solution.isValid(s) == expected


def test_case_4():
    s = '([])'
    expected = True
    assert solution.isValid(s) == expected
