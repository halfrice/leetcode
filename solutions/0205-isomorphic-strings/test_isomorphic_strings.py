from isomorphic_strings import Solution

solution = Solution()


def test_case_1():
    s = 'egg'
    t = 'add'
    expected = True
    assert solution.isIsomorphic(s, t) == expected


def test_case_2():
    s = 'foo'
    t = 'bar'
    expected = False
    assert solution.isIsomorphic(s, t) == expected


def test_case_3():
    s = 'paper'
    t = 'title'
    expected = True
    assert solution.isIsomorphic(s, t) == expected


def test_case_4():
    s = 'paper'
    t = 'tiger'
    expected = False
    assert solution.isIsomorphic(s, t) == expected


def test_case_5():
    s = 'bbbaaaba'
    t = 'aaabbbba'
    expected = False
    assert solution.isIsomorphic(s, t) == expected


def test_case_6():
    s = 'badc'
    t = 'baba'
    expected = False
    assert solution.isIsomorphic(s, t) == expected
