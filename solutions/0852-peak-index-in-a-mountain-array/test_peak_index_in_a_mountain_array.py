from peak_index_in_a_mountain_array import Solution

solution = Solution()


def test_case_1():
    arr = [0, 1, 0]
    expected = 1
    assert solution.peakIndexInMountainArray(arr) == expected


def test_case_2():
    arr = [0, 2, 1, 0]
    expected = 1
    assert solution.peakIndexInMountainArray(arr) == expected


def test_case_3():
    arr = [0, 10, 5, 2]
    expected = 1
    assert solution.peakIndexInMountainArray(arr) == expected
