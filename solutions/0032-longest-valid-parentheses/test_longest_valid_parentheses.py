from longest_valid_parentheses import Solution

solution = Solution()


def test_case_1():
    s = '(()'
    expected = 2
    assert solution.longestValidParentheses(s) == expected


def test_case_2():
    s = ')()())'
    expected = 4
    assert solution.longestValidParentheses(s) == expected


def test_case_3():
    s = ''
    expected = 0
    assert solution.longestValidParentheses(s) == expected


def test_case_4():
    s = '(()())'
    expected = 6
    assert solution.longestValidParentheses(s) == expected


def test_case_custom_case_1():
    s = '(()(())'
    expected = 6
    assert solution.longestValidParentheses(s) == expected
