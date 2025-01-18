from jump_game import Solution

solution = Solution()


def test_case_1():
    nums = [2, 3, 1, 1, 4]
    expected = True
    assert solution.canJump(nums) == expected


def test_case_2():
    nums = [3, 2, 1, 0, 4]
    expected = False
    assert solution.canJump(nums) == expected
