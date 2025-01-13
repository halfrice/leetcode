from merge_strings_alternately import Solution

solution = Solution()


def test_case_1():
    word1 = 'abc'
    word2 = 'pqr'
    expected = 'apbqcr'
    assert solution.mergeAlternately(word1, word2) == expected


def test_case_2():
    word1 = 'ab'
    word2 = 'pqrs'
    expected = 'apbqrs'
    assert solution.mergeAlternately(word1, word2) == expected


def test_case_3():
    word1 = 'abcd'
    word2 = 'pq'
    expected = 'apbqcd'
    assert solution.mergeAlternately(word1, word2) == expected
