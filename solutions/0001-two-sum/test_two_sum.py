# test_two_sum.py

from two_sum import Solution

s = Solution()


def test_case_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert s.twoSum(nums, target) == expected


def test_case_2():
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert s.twoSum(nums, target) == expected


def test_case_3():
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert s.twoSum(nums, target) == expected
