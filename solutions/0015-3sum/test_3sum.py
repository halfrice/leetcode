import importlib

sum = importlib.import_module('3sum')

solution = sum.Solution()


def test_case_1():
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum(nums) == expected


def test_case_2():
    nums = [0, 1, 1]
    expected = []
    assert solution.threeSum(nums) == expected


def test_case_3():
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]
    assert solution.threeSum(nums) == expected
