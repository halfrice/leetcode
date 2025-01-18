from remove_duplicates_from_sorted_array_ii import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 1, 2, 2, 3]
    expected = 5
    assert solution.removeDuplicates(nums) == expected
    assert nums[:expected] == [1, 1, 2, 2, 3]


def test_case_2():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected = 7
    assert solution.removeDuplicates(nums) == expected
    assert nums[:expected] == [0, 0, 1, 1, 2, 3, 3]
