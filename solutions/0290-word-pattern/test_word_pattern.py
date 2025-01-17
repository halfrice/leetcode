from word_pattern import Solution

solution = Solution()


def test_case_1():
    pattern = 'abba'
    s = 'dog cat cat dog'
    expected = True
    assert solution.wordPattern(pattern, s) == expected


def test_case_2():
    pattern = 'abba'
    s = 'dog cat cat fish'
    expected = False
    assert solution.wordPattern(pattern, s) == expected


def test_case_3():
    pattern = 'aaaa'
    s = 'dog cat cat dog'
    expected = False
    assert solution.wordPattern(pattern, s) == expected
