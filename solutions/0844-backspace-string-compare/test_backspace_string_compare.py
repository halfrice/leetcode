from backspace_string_compare import Solution

solution = Solution()


def test_case_1():
    s = 'ab#c'
    t = 'ad#c'
    expected = True
    assert solution.backspaceCompare(s, t) == expected


def test_case_2():
    s = 'ab##'
    t = 'c#d#'
    expected = True
    assert solution.backspaceCompare(s, t) == expected


def test_case_3():
    s = 'a#c'
    t = 'b'
    expected = False
    assert solution.backspaceCompare(s, t) == expected


def test_case_4():
    s = 'a'
    t = 'aa#a'
    expected = False
    assert solution.backspaceCompare(s, t) == expected
