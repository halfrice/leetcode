from is_subsequence import Solution

solution = Solution()


def test_case_1():
    s = 'abc'
    t = 'ahbgdc'
    expected = True
    assert solution.isSubsequence(s, t) == expected


def test_case_2():
    s = 'axc'
    t = 'ahbgdc'
    expected = False
    assert solution.isSubsequence(s, t) == expected


def test_case_3():
    s = 'abc'
    t = ''
    expected = False
    assert solution.isSubsequence(s, t) == expected


def test_case_4():
    s = ''
    t = ''
    expected = True
    assert solution.isSubsequence(s, t) == expected
