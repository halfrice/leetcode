from longest_consecutive_sequence import Solution

solution = Solution()


def test_case_1():
    nums = [100, 4, 200, 1, 3, 2]
    expected = 4
    assert solution.longestConsecutive(nums) == expected


def test_case_2():
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected = 9
    assert solution.longestConsecutive(nums) == expected


def test_custom_case_1():
    nums = [1, 2, 0, 1]
    expected = 3
    assert solution.longestConsecutive(nums) == expected


def test_custom_case_2():
    nums = [0, 0]
    expected = 1
    assert solution.longestConsecutive(nums) == expected


def test_custom_case_3():
    nums = []
    expected = 0
    assert solution.longestConsecutive(nums) == expected
