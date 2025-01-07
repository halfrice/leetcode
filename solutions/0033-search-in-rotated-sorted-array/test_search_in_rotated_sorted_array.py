from search_in_rotated_sorted_array import Solution

solution = Solution()


def test_case_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    expected = 4
    assert solution.search(nums, target) == expected


def test_case_2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1
    assert solution.search(nums, target) == expected


def test_case_3():
    nums = [1]
    target = 0
    expected = -1
    assert solution.search(nums, target) == expected


def test_custom_case_1():
    nums = [1]
    target = 1
    expected = 0
    assert solution.search(nums, target) == expected


def test_custom_case_2():
    nums = [1, 3]
    target = 3
    expected = 1
    assert solution.search(nums, target) == expected
