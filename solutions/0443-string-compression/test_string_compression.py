from string_compression import Solution

solution = Solution()


def test_case_1():
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    expected = 6
    assert solution.compress(chars) == expected


def test_case_2():
    chars = ['a']
    expected = 1
    assert solution.compress(chars) == expected


def test_case_3():
    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    expected = 4
    assert solution.compress(chars) == expected
