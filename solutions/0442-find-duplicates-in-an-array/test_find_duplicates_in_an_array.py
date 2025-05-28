from find_duplicates_in_an_array import Solution

solution = Solution()


def test_case_1():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [2, 3]
    assert solution.findDuplicates(nums).sort() == expected.sort()


def test_case_2():
    nums = [1, 1, 2]
    expected = [1]
    assert solution.findDuplicates(nums).sort() == expected.sort()


def test_case_3():
    nums = [1]
    expected = []
    assert solution.findDuplicates(nums).sort() == expected.sort()
