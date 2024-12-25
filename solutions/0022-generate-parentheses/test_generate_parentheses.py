from generate_parentheses import Solution

solution = Solution()


def test_case_1():
    n = 3
    expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert solution.generateParenthesis(n) == expected


def test_case_2():
    n = 1
    expected = ['()']
    assert solution.generateParenthesis(n) == expected


def test_custom_case_1():
    n = 2
    expected = ['(())', '()()']
    assert solution.generateParenthesis(n) == expected
