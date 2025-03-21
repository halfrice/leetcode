from decode_string import Solution

solution = Solution()


def test_case_1():
    s = '3[a]2[bc]'
    expected = 'aaabcbc'
    assert solution.decodeString(s) == expected


def test_case_2():
    s = '3[a2[c]]'
    expected = 'accaccacc'
    assert solution.decodeString(s) == expected


def test_case_3():
    s = '2[abc]3[cd]ef'
    expected = 'abcabccdcdcdef'
    assert solution.decodeString(s) == expected
