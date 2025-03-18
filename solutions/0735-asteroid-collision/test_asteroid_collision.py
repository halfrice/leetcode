from asteroid_collision import Solution

solution = Solution()


def test_case_1():
    asteroids = [5, 10, -5]
    expected = [5, 10]
    assert solution.asteroidCollision(asteroids) == expected


def test_case_2():
    asteroids = [8, -8]
    expected = []
    assert solution.asteroidCollision(asteroids) == expected


def test_case_3():
    asteroids = [10, 2, -5]
    expected = [10]
    assert solution.asteroidCollision(asteroids) == expected


def test_case_4():
    asteroids = [-2, -1, 1, 2]
    expected = [-2, -1, 1, 2]
    assert solution.asteroidCollision(asteroids) == expected
