from reverse_words_in_a_string import Solution

solution = Solution()


def test_case_1():
    s = 'the sky is blue'
    expected = 'blue is sky the'
    assert solution.reverseWords(s) == expected


def test_case_2():
    s = '  hello world  '
    expected = 'world hello'
    assert solution.reverseWords(s) == expected


def test_case_3():
    s = 'a good   example'
    expected = 'example good a'
    assert solution.reverseWords(s) == expected
