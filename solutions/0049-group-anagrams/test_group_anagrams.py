from group_anagrams import Solution

solution = Solution()


def test_case_1():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    expected = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
    assert solution.groupAnagrams(strs) == expected


def test_case_2():
    strs = ['']
    expected = [['']]
    assert solution.groupAnagrams(strs) == expected


def test_case_3():
    strs = ['a']
    expected = [['a']]
    assert solution.groupAnagrams(strs) == expected
