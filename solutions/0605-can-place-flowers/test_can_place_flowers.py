from can_place_flowers import Solution

solution = Solution()


def test_case_1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n) == expected


def test_case_2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    expected = False
    assert solution.canPlaceFlowers(flowerbed, n) == expected


def test_case_3():
    flowerbed = [0, 0, 1, 0, 0]
    n = 1
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n) == expected
