from longest_repeating_character_replacement import Solution

solution = Solution()


def test_case_1():
    s = 'ABAB'
    k = 2
    expected = 4
    assert solution.characterReplacement(s, k) == expected


def test_case_2():
    s = 'AABABBA'
    k = 1
    expected = 4
    assert solution.characterReplacement(s, k) == expected
