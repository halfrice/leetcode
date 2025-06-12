from build_array_from_permutation import Solution

solution = Solution()


def test_case_1():
    nums = [0, 2, 1, 5, 3, 4]
    expected = [0, 1, 2, 4, 5, 3]
    assert solution.buildArray(nums) == expected


def test_case_2():
    nums = [5, 0, 1, 2, 3, 4]
    expected = [4, 5, 0, 1, 2, 3]
    assert solution.buildArray(nums) == expected
