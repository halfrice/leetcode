from house_robber import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 1]
    expected = 4
    assert solution.rob(nums) == expected


def test_case_2():
    nums = [2, 7, 9, 3, 1]
    expected = 12
    assert solution.rob(nums) == expected
