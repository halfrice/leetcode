from first_missing_positive import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 0]
    expected = 3
    assert solution.firstMissingPositive(nums) == expected


def test_case_2():
    nums = [3, 4, -1, 1]
    expected = 2
    assert solution.firstMissingPositive(nums) == expected


def test_case_3():
    nums = [7, 8, 9, 11, 12]
    expected = 1
    assert solution.firstMissingPositive(nums) == expected
