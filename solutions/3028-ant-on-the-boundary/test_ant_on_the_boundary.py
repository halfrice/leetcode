from ant_on_the_boundary import Solution

solution = Solution()


def test_case_1():
    nums = [2, 3, -5]
    expected = 1
    assert solution.returnToBoundaryCount(nums) == expected


def test_case_2():
    nums = [3, 2, -3, -4]
    expected = 0
    assert solution.returnToBoundaryCount(nums) == expected
