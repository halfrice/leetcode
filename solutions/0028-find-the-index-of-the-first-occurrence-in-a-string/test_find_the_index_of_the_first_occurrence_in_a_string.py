from find_the_index_of_the_first_occurrence_in_a_string import Solution

solution = Solution()


def test_case_1():
    haystack = 'sadbutsad'
    needle = 'sad'
    expected = 0
    assert solution.strStr(haystack, needle) == expected


def test_case_2():
    haystack = 'leetcode'
    needle = 'leeto'
    expected = -1
    assert solution.strStr(haystack, needle) == expected
