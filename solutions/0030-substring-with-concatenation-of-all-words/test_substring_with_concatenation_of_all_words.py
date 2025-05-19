from substring_with_concatenation_of_all_words import Solution

solution = Solution()


def test_case_1():
    s = 'barfoothefoobarman'
    words = ['foo', 'bar']
    expected = [0, 9]
    assert solution.findSubstring(s, words) == expected


def test_case_2():
    s = 'wordgoodgoodgoodbestword'
    words = ['word', 'good', 'best', 'word']
    expected = []
    assert solution.findSubstring(s, words) == expected


def test_case_3():
    s = 'barfoofoobarthefoobarman'
    words = ['bar', 'foo', 'the']
    expected = [6, 9, 12]
    assert solution.findSubstring(s, words) == expected

