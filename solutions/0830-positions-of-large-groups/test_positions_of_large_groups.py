from positions_of_large_groups import Solution

solution = Solution()


def test_case_1():
    s = 'abbxxxxzzy'
    expected = [[3, 6]]
    assert solution.largeGroupPositions(s) == expected


def test_case_2():
    s = 'abc'
    expected = []
    assert solution.largeGroupPositions(s) == expected


def test_case_3():
    s = 'abcdddeeeeaabbbcd'
    expected = [[3, 5], [6, 9], [12, 14]]
    assert solution.largeGroupPositions(s) == expected


def test_case_4():
    s = 'aaa'
    expected = [[0, 2]]
    assert solution.largeGroupPositions(s) == expected
