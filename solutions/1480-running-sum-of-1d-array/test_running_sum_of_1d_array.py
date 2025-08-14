from running_sum_of_1d_array import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4]
    expected = [1, 3, 6, 10]
    assert solution.runningSum(nums) == expected


def test_case_2():
    nums = [1, 1, 1, 1, 1]
    expected = [1, 2, 3, 4, 5]
    assert solution.runningSum(nums) == expected


def test_case_3():
    nums = [3, 1, 2, 10, 1]
    expected = [3, 4, 6, 16, 17]
    assert solution.runningSum(nums) == expected
