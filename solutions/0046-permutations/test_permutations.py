from permutations import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert solution.permute(nums) == expected


def test_case_2():
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    assert solution.permute(nums) == expected


def test_case_3():
    nums = [1]
    expected = [[1]]
    assert solution.permute(nums) == expected
