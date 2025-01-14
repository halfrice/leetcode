from valid_palindrome import Solution

solution = Solution()


def test_case_1():
    s = 'A man, a plan, a canal: Panama'
    expected = True
    assert solution.isPalindrome(s) == expected


def test_case_2():
    s = 'race a car'
    expected = False
    assert solution.isPalindrome(s) == expected


def test_case_3():
    s = ' '
    expected = True
    assert solution.isPalindrome(s) == expected


def test_case_4():
    s = 'ab_a'
    expected = True
    assert solution.isPalindrome(s) == expected


def test_case_5():
    s = '.,'
    expected = True
    assert solution.isPalindrome(s) == expected
