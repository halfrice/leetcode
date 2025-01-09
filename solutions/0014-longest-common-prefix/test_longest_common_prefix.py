from longest_common_prefix import Solution

solution = Solution()


def test_case_1():
    strs = ['flower', 'flow', 'flight']
    expected = 'fl'
    assert solution.longestCommonPrefix(strs) == expected


def test_case_2():
    strs = ['dog', 'racecar', 'car']
    expected = ''
    assert solution.longestCommonPrefix(strs) == expected


def test_custom_case_1():
    strs = ['']
    expected = ''
    assert solution.longestCommonPrefix(strs) == expected
