# test_contains_duplicate.py

from contains_duplicate import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 1]
    expected = True
    assert solution.containsDuplicate(nums) == expected


def test_case_2():
    nums = [1, 2, 3, 4]
    expected = False
    assert solution.containsDuplicate(nums) == expected


def test_case_3():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected = True
    assert solution.containsDuplicate(nums) == expected
