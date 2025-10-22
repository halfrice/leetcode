from valid_mountain_array import Solution

solution = Solution()


def test_case_1():
    arr = [2, 1]
    expected = False
    assert solution.validMountainArray(arr) == expected


def test_case_2():
    arr = [3, 5, 5]
    expected = False
    assert solution.validMountainArray(arr) == expected


def test_case_3():
    arr = [0, 3, 2, 1]
    expected = True
    assert solution.validMountainArray(arr) == expected


def test_case_4():
    arr = [1, 4, 5, 3, 6, 3, 2, 1]
    expected = False
    assert solution.validMountainArray(arr) == expected
