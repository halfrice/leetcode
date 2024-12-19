from evaluate_reverse_polish_notation import Solution

solution = Solution()


def test_case_1():
    tokens = ['2', '1', '+', '3', '*']
    expected = 9
    assert solution.evalRPN(tokens) == expected


def test_case_2():
    tokens = ['4', '13', '5', '/', '+']
    expected = 6
    assert solution.evalRPN(tokens) == expected


def test_case_3():
    tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    expected = 22
    assert solution.evalRPN(tokens) == expected
