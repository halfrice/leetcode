from determine_if_two_strings_are_close import Solution

solution = Solution()


def test_case_1():
    word1 = 'abc'
    word2 = 'bca'
    expected = True
    assert solution.closeStrings(word1, word2) == expected


def test_case_2():
    word1 = 'a'
    word2 = 'aa'
    expected = False
    assert solution.closeStrings(word1, word2) == expected


def test_case_3():
    word1 = 'cabbba'
    word2 = 'abbccc'
    expected = True
    assert solution.closeStrings(word1, word2) == expected
