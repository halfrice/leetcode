from importlib import import_module

solution = import_module('3sum_closest').Solution()


def test_case_1():
    nums = [-1, 2, 1, -4]
    target = 1
    expected = 2
    assert solution.threeSumClosest(nums, target) == expected


def test_case_2():
    nums = [0, 0, 0]
    target = 1
    expected = 0
    assert solution.threeSumClosest(nums, target) == expected
