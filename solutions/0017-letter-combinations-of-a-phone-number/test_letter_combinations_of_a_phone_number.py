from letter_combinations_of_a_phone_number import Solution

solution = Solution()


def test_case_1():
    digits = '23'
    expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert solution.letterCombinations(digits) == expected


def test_case_2():
    digits = ''
    expected = []
    assert solution.letterCombinations(digits) == expected


def test_case_3():
    digits = '2'
    expected = ['a', 'b', 'c']
    assert solution.letterCombinations(digits) == expected
