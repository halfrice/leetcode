from rotate_string import Solution

solution = Solution()


def test_case_1():
    s = 'abcde'
    goal = 'cdeab'
    expected = True
    assert solution.rotateString(s, goal) == expected


def test_case_2():
    s = 'abcde'
    goal = 'abced'
    expected = False
    assert solution.rotateString(s, goal) == expected
