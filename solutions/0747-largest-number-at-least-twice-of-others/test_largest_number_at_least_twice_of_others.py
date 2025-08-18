from largest_number_at_least_twice_of_others import Solution

solution = Solution()


def test_case_1():
    nums = [3, 6, 1, 0]
    expected = 1
    assert solution.dominantIndex(nums) == expected


def test_case_2():
    nums = [1, 2, 3, 4]
    expected = -1
    assert solution.dominantIndex(nums) == expected


def test_case_3():
    nums = [0, 0, 3, 2]
    expected = -1
    assert solution.dominantIndex(nums) == expected
