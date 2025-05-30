from wildcard_matching import Solution

solution = Solution()


def test_case_1():
    s = 'aa'
    p = 'a'
    expected = False
    assert solution.isMatch(s, p) == expected


def test_case_2():
    s = 'aa'
    p = '*'
    expected = True
    assert solution.isMatch(s, p) == expected


def test_case_3():
    s = 'cb'
    p = '?a'
    expected = False
    assert solution.isMatch(s, p) == expected
