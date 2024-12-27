from container_with_most_water import Solution

solution = Solution()


def test_case_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    assert solution.maxArea(height) == expected


def test_case_2():
    height = [1, 1]
    expected = 1
    assert solution.maxArea(height) == expected


def test_custom_case_1():
    height = [1, 2, 1]
    expected = 2
    assert solution.maxArea(height) == expected


def test_custom_case_2():
    height = [1, 2, 3, 4]
    expected = 4
    assert solution.maxArea(height) == expected


def test_custom_case_3():
    height = [2, 3, 4, 5, 18, 17, 6]
    expected = 17
    assert solution.maxArea(height) == expected


def test_custom_case_4():
    height = [7, 10, 6, 2, 5, 4, 8, 3, 7]
    expected = 56
    assert solution.maxArea(height) == expected
