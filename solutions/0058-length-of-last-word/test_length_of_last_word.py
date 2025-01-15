from length_of_last_word import Solution

solution = Solution()


def test_case_1():
    s = 'Hello World'
    expected = 5
    assert solution.lengthOfLastWord(s) == expected


def test_case_2():
    s = '   fly me   to   the moon  '
    expected = 4
    assert solution.lengthOfLastWord(s) == expected


def test_case_3():
    s = 'luffy is still joyboy'
    expected = 6
    assert solution.lengthOfLastWord(s) == expected
