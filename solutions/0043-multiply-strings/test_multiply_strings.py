from multiply_strings import Solution

solution = Solution()


def test_case_1():
    num1 = '2'
    num2 = '3'
    expected = '6'
    assert solution.multiply(num1, num2) == expected


def test_case_2():
    num1 = '123'
    num2 = '456'
    expected = '56088'
    assert solution.multiply(num1, num2) == expected
