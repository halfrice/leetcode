from regular_expression_matching import Solution

solution = Solution()


def test_case_1():
    s = 'aa'
    p = 'a'
    expected = False
    assert solution.isMatch(s, p) == expected


def test_case_2():
    s = 'aa'
    p = 'a*'
    expected = True
    assert solution.isMatch(s, p) == expected


def test_case_3():
    s = 'ab'
    p = '.*'
    expected = True
    assert solution.isMatch(s, p) == expected


def test_custom_case_1():
    s = 'zyzz'
    p = 'x*..z*'
    expected = True
    assert solution.isMatch(s, p) == expected


def test_custom_case_2():
    s = ''
    p = ''
    expected = True
    assert solution.isMatch(s, p) == expected
