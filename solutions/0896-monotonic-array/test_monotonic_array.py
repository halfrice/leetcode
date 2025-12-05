from monotonic_array import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 2, 3]
    expected = True
    assert solution.isMonotonic(nums) == expected


def test_case_2():
    nums = [6, 5, 4, 4]
    expected = True
    assert solution.isMonotonic(nums) == expected


def test_case_3():
    nums = [1, 3, 2]
    expected = False
    assert solution.isMonotonic(nums) == expected
