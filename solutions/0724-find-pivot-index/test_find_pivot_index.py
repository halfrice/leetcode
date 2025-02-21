from find_pivot_index import Solution

solution = Solution()


def test_case_1():
    nums = [1, 7, 3, 6, 5, 6]
    expected = 3
    assert solution.pivotIndex(nums) == expected


def test_case_2():
    nums = [1, 2, 3]
    expected = -1
    assert solution.pivotIndex(nums) == expected


def test_case_3():
    nums = [2, 1, -1]
    expected = 0
    assert solution.pivotIndex(nums) == expected
