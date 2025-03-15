from max_number_of_k_sum_pairs import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4]
    k = 5
    expected = 2
    assert solution.maxOperations(nums, k) == expected


def test_case_2():
    nums = [3, 1, 3, 4, 3]
    k = 6
    expected = 1
    assert solution.maxOperations(nums, k) == expected
