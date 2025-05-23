from find_first_and_last_position_of_element_in_sorted_array import Solution

solution = Solution()


def test_case_1():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    assert solution.searchRange(nums, target) == expected


def test_case_2():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]
    assert solution.searchRange(nums, target) == expected


def test_case_3():
    nums = []
    target = 0
    expected = [-1, -1]
    assert solution.searchRange(nums, target) == expected
