from rotate_array import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    solution.rotate(nums, k)
    assert nums == expected


def test_case_2():
    nums = [-1, -100, 3, 99]
    k = 2
    expected = [3, 99, -1, -100]
    solution.rotate(nums, k)
    assert nums == expected
