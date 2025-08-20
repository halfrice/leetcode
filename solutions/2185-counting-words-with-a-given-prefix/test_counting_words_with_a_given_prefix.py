from counting_words_with_a_given_prefix import Solution

solution = Solution()


def test_case_1():
    words = ['pay', 'attention', 'practice', 'attend']
    pref = 'at'
    expected = 2
    assert solution.prefixCount(words, pref) == expected


def test_case_2():
    words = ['leetcode', 'win', 'loops', 'success']
    pref = 'code'
    expected = 0
    assert solution.prefixCount(words, pref) == expected
