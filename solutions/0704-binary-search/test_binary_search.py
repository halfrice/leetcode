from binary_search import Solution

solution = Solution()


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    expected = 4
    assert solution.search(nums, target) == expected


def test_case_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    assert solution.search(nums, target) == expected
