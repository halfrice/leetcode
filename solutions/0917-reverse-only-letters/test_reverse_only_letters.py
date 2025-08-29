from reverse_only_letters import Solution

solution = Solution()


def test_case_1():
    s = 'ab-cd'
    expected = 'dc-ba'
    assert solution.reverseOnlyLetters(s) == expected


def test_case_2():
    s = 'a-bC-dEf-ghIj'
    expected = 'j-Ih-gfE-dCba'
    assert solution.reverseOnlyLetters(s) == expected


def test_case_3():
    s = 'Test1ng-Leet=code-Q!'
    expected = 'Qedo1ct-eeLg=ntse-T!'
    assert solution.reverseOnlyLetters(s) == expected
