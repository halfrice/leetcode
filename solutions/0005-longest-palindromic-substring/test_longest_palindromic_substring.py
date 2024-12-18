from longest_palindromic_substring import Solution

solution = Solution()


def test_case_1():
    s = 'babad'
    expected = 'bab'  # or 'aba'
    assert solution.longestPalindrome(s) == expected


def test_case_2():
    s = 'cbbd'
    expected = 'bb'
    assert solution.longestPalindrome(s) == expected


def test_custom_case_1():
    s = 'racecar'
    expected = 'racecar'
    assert solution.longestPalindrome(s) == expected


def test_custom_case_2():
    s = 'abbazezalphaduethoohbookkoob'
    expected = 'bookkoob'
    assert solution.longestPalindrome(s) == expected


def test_custom_case_3():
    s = 'abbazezabookkoob'
    expected = 'bookkoob'
    assert solution.longestPalindrome(s) == expected


def test_custom_case_4():
    s = 'banananananananananananananananananananananana'
    expected = 'anananananananananananananananananananananana'
    assert solution.longestPalindrome(s) == expected
