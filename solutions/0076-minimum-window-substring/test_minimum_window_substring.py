from minimum_window_substring import Solution


solution = Solution()


def test_case_1():
    s = 'ADOBECODEBANC'
    t = 'ABC'
    expected = 'BANC'
    assert solution.minWindow(s, t) == expected


def test_case_2():
    s = 'a'
    t = 'a'
    expected = 'a'
    assert solution.minWindow(s, t) == expected


def test_case_3():
    s = 'a'
    t = 'aa'
    expected = ''
    assert solution.minWindow(s, t) == expected
