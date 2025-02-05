from move_zeroes import Solution

solution = Solution()


def test_case_1():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    solution.moveZeroes(nums)
    assert nums == expected


def test_case_2():
    nums = [0]
    expected = [0]
    solution.moveZeroes(nums)
    assert nums == expected


def test_case_3():
    nums = [2, 1]
    expected = [2, 1]
    solution.moveZeroes(nums)
    assert nums == expected


def test_case_4():
    nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    expected = [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    solution.moveZeroes(nums)
    assert nums == expected
