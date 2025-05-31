from permutations_ii import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 2]
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert solution.permuteUnique(nums) == expected


def test_case_2():
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert solution.permuteUnique(nums) == expected
