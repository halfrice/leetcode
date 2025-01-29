from candy import Solution

solution = Solution()


def test_case_1():
    ratings = [1, 0, 2]
    expected = 5
    assert solution.candy(ratings) == expected


def test_case_2():
    ratings = [1, 2, 2]
    expected = 4
    assert solution.candy(ratings) == expected
