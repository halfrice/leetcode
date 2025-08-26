from maximum_number_of_balloons import Solution

solution = Solution()


def test_case_1():
    text = 'nlaebolko'
    expected = 1
    assert solution.maxNumberOfBalloons(text) == expected


def test_case_2():
    text = 'loonbalxballpoon'
    expected = 2
    assert solution.maxNumberOfBalloons(text) == expected


def test_case_3():
    text = 'leetcode'
    expected = 0
    assert solution.maxNumberOfBalloons(text) == expected


def test_case_4():
    text = 'loonbalxballpoonballoo'
    expected = 2
    assert solution.maxNumberOfBalloons(text) == expected
