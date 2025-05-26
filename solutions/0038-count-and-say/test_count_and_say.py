from count_and_say import Solution

solution = Solution()


def test_case_1():
    n = 4
    expected = '1211'
    assert solution.countAndSay(n) == expected


def test_case_2():
    n = 1
    expected = '1'
    assert solution.countAndSay(n) == expected


def test_case_3():
    n = 5
    expected = '111221'
    assert solution.countAndSay(n) == expected
