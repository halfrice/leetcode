from longest_subarray_of_1s_after_deleting_one_element import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 0, 1]
    expected = 3
    assert solution.longestSubarray(nums) == expected


def test_case_2():
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    expected = 5
    assert solution.longestSubarray(nums) == expected


def test_case_3():
    nums = [1, 1, 1]
    expected = 2
    assert solution.longestSubarray(nums) == expected
