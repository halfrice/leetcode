from jump_game_ii import Solution

solution = Solution()


def test_case_1():
    nums = [2, 3, 1, 1, 4]
    expected = 2
    assert solution.jump(nums) == expected


def test_case_2():
    nums = [2, 3, 0, 1, 4]
    expected = 2
    assert solution.jump(nums) == expected
