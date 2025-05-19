from next_permutation import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3]
    expected = [1, 3, 2]
    solution.nextPermutation(nums)
    assert nums == expected


def test_case_2():
    nums = [3, 2, 1]
    expected = [1, 2, 3]
    solution.nextPermutation(nums)
    assert nums == expected


def test_case_3():
    nums = [1, 1, 5]
    expected = [1, 5, 1]
    solution.nextPermutation(nums)
    assert nums == expected
