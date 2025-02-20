from reverse_vowels_of_a_string import Solution

solution = Solution()


def test_case_1():
    s = 'IceCreAm'
    expected = 'AceCreIm'
    assert solution.reverseVowels(s) == expected


def test_case_2():
    s = 'leetcode'
    expected = 'leotcede'
    assert solution.reverseVowels(s) == expected
