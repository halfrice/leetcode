from greatest_common_divisor_of_strings import Solution

solution = Solution()


def test_case_1():
    str1 = 'ABCABC'
    str2 = 'ABC'
    expected = 'ABC'
    assert solution.gcdOfStrings(str1, str2) == expected


def test_case_2():
    str1 = 'ABABAB'
    str2 = 'ABAB'
    expected = 'AB'
    assert solution.gcdOfStrings(str1, str2) == expected


def test_case_3():
    str1 = 'LEET'
    str2 = 'CODE'
    expected = ''
    assert solution.gcdOfStrings(str1, str2) == expected


def test_case_4():
    str1 = 'TAUXXTAUXXTAUXXTAUXXTAUXX'
    str2 = 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'
    expected = 'TAUXX'
    assert solution.gcdOfStrings(str1, str2) == expected
