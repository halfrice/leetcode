from sort_array_by_parity_ii import Solution

solution = Solution()


def test_case_1():
    nums = [4, 2, 5, 7]
    expected = [4, 5, 2, 7]
    assert solution.sortArrayByParityII(nums) == expected


def test_case_2():
    nums = [2, 3]
    expected = [2, 3]
    assert solution.sortArrayByParityII(nums) == expected
