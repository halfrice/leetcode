from add_binary import Solution

solution = Solution()


def test_case_1():
    a = '11'
    b = '1'
    expected = '100'
    assert solution.addBinary(a, b) == expected


def test_case_2():
    a = '1010'
    b = '1011'
    expected = '10101'
    assert solution.addBinary(a, b) == expected
