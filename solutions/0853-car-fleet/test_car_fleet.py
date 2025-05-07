from car_fleet import Solution

solution = Solution()


def test_case_1():
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    expected = 3
    assert solution.carFleet(target, position, speed) == expected


def test_case_2():
    target = 10
    position = [3]
    speed = [3]
    expected = 1
    assert solution.carFleet(target, position, speed) == expected


def test_case_3():
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    expected = 1
    assert solution.carFleet(target, position, speed) == expected
