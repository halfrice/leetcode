from maximum_number_of_vowels_in_a_substring_of_given_length import Solution

solution = Solution()


def test_case_1():
    s = 'abciiidef'
    k = 3
    expected = 3
    assert solution.maxVowels(s, k) == expected


def test_case_2():
    s = 'aeiou'
    k = 2
    expected = 2
    assert solution.maxVowels(s, k) == expected


def test_case_3():
    s = 'leetcode'
    k = 3
    expected = 2
    assert solution.maxVowels(s, k) == expected
