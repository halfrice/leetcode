from find_the_highest_altitude import Solution

solution = Solution()


def test_case_1():
    gain = [-5, 1, 5, 0, -7]
    expected = 1
    assert solution.largestAltitude(gain) == expected


def test_case_2():
    gain = [-4, -3, -2, -1, 4, 3, 2]
    expected = 0
    assert solution.largestAltitude(gain) == expected
