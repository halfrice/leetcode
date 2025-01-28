from minimum_size_subarray_sum import Solution

solution = Solution()


def test_case_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = 2
    assert solution.minSubArrayLen(target, nums) == expected


def test_case_2():
    target = 4
    nums = [1, 4, 4]
    expected = 1
    assert solution.minSubArrayLen(target, nums) == expected


def test_case_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = 0
    assert solution.minSubArrayLen(target, nums) == expected
