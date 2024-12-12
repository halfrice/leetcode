# test_longest_substring_without_repeating_charaters.py

from longest_substring_without_repeating_characters import Solution

solution = Solution()


def test_case_1():
    s = 'abcabcbb'
    expected = 3
    assert solution.lengthOfLongestSubstring(s) == expected


def test_case_2():
    s = 'bbbbb'
    expected = 1
    assert solution.lengthOfLongestSubstring(s) == expected


def test_case_3():
    s = 'pwwkew'
    expected = 3
    assert solution.lengthOfLongestSubstring(s) == expected
