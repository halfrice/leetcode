from maximum_subarray import Solution

solution = Solution()


def test_case_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    assert solution.maxSubArray(nums) == expected


def test_case_2():
    nums = [1]
    expected = 1
    assert solution.maxSubArray(nums) == expected


def test_case_3():
    nums = [5, 4, -1, 7, 8]
    expected = 23
    assert solution.maxSubArray(nums) == expected
