from maximum_average_subarray_i import Solution

solution = Solution()


def test_case_1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected = 12.75000
    assert solution.findMaxAverage(nums, k) == expected


def test_case_2():
    nums = [5]
    k = 1
    expected = 5.00000
    assert solution.findMaxAverage(nums, k) == expected
