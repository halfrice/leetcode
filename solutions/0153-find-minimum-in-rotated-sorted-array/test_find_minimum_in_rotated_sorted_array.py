from find_minimum_in_rotated_sorted_array import Solution

solution = Solution()


def test_case_1():
    nums = [3, 4, 5, 1, 2]
    expected = 1
    assert solution.findMin(nums) == expected


def test_case_2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    expected = 0
    assert solution.findMin(nums) == expected


def test_case_3():
    nums = [11, 13, 15, 17]
    expected = 11
    assert solution.findMin(nums) == expected
