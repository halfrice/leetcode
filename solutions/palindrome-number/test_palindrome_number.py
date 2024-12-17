# test_palindrome_number.py

from palindrome_number import Solution

solution = Solution()


def test_case_1():
    x = 121
    expected = True
    assert solution.isPalindrome(x) == expected


def test_case_2():
    x = -121
    expected = False
    assert solution.isPalindrome(x) == expected


def test_case_3():
    x = 10
    expected = False
    assert solution.isPalindrome(x) == expected


def test_custom_case_1():
    x = 987656789
    expected = True
    assert solution.isPalindrome(x) == expected


def test_custom_case_2():
    x = 5000
    expected = False
    assert solution.isPalindrome(x) == expected
