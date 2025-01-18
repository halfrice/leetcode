from remove_duplicates import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 2]
    expected = 2
    assert solution.removeDuplicates(nums) == expected
    assert nums[:expected] == [1, 2]


def test_case_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = 5
    assert solution.removeDuplicates(nums) == expected
    assert nums[:expected] == [0, 1, 2, 3, 4]
