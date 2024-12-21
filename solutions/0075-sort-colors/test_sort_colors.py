from sort_colors import Solution

solution = Solution()


def test_case_1():
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected


def test_case_2():
    nums = [2, 0, 1]
    expected = [0, 1, 2]
    solution.sortColors(nums)
    assert nums == expected


def test_case_3():
    nums = [0, 1, 2, 2, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == expected
