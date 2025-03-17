from removing_stars_from_a_string import Solution

solution = Solution()


def test_case_1():
    s = 'leet**cod*e'
    expected = 'lecoe'
    assert solution.removeStars(s) == expected


def test_case_2():
    s = 'erase*****'
    expected = ''
    assert solution.removeStars(s) == expected
