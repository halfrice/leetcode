from happy_number import Solution

solution = Solution()


def test_case_1():
    n = 19
    expected = True
    assert solution.isHappy(n) == expected
