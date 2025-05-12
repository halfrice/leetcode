from importlib import import_module

solution = import_module('4sum').Solution()


def test_case_1():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert solution.fourSum(nums, target) == expected


def test_case_2():
    nums = [2, 2, 2, 2, 2]
    target = 8
    expected = [[2, 2, 2, 2]]
    assert solution.fourSum(nums, target) == expected
