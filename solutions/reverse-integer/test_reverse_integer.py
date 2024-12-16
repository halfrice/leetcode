# test_reverse_integer.py


from reverse_integer import Solution

solution = Solution()


def test_case_1():
    x = 123
    expected = 321
    assert solution.reverse(x) == expected


def test_case_2():
    x = -123
    expected = -321
    assert solution.reverse(x) == expected


def test_case_3():
    x = 120
    expected = 21
    assert solution.reverse(x) == expected
