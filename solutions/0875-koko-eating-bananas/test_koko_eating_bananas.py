from koko_eating_bananas import Solution

solution = Solution()


def test_case_1():
    piles = [3, 6, 7, 11]
    h = 8
    expected = 4
    assert solution.minEatingSpeed(piles, h) == expected


def test_case_2():
    piles = [30, 11, 23, 4, 20]
    h = 5
    expected = 30
    assert solution.minEatingSpeed(piles, h) == expected


def test_case_3():
    piles = [30, 11, 23, 4, 20]
    h = 6
    expected = 23
    assert solution.minEatingSpeed(piles, h) == expected
