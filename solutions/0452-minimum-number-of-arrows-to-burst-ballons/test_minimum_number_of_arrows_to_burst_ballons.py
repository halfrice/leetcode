from minimum_number_of_arrows_to_burst_ballons import Solution

solution = Solution()


def test_case_1():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected = 2
    assert solution.findMinArrowShots(points) == expected


def test_case_2():
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected = 4
    assert solution.findMinArrowShots(points) == expected


def test_case_3():
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expected = 2
    assert solution.findMinArrowShots(points) == expected
