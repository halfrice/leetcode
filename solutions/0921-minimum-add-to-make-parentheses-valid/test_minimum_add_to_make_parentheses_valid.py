from minimum_add_to_make_parentheses_valid import Solution

solution = Solution()


def test_case_1():
    s = '())'
    expected = 1
    assert solution.minAddToMakeValid(s) == expected


def test_case_2():
    s = '((('
    expected = 3
    assert solution.minAddToMakeValid(s) == expected
