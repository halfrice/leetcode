from max_consecutive_ones_iii import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    expected = 6
    assert solution.longestOnes(nums, k) == expected


def test_case_2():
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    expected = 10
    assert solution.longestOnes(nums, k) == expected
