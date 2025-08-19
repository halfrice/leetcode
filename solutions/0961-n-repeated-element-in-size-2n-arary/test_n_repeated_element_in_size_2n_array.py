from n_repeated_element_in_size_2n_array import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 3]
    expected = 3
    assert solution.repeatedNTimes(nums) == expected


def test_case_2():
    nums = [2, 1, 2, 5, 3, 2]
    expected = 2
    assert solution.repeatedNTimes(nums) == expected


def test_case_3():
    nums = [5, 1, 5, 2, 5, 3, 5, 4]
    expected = 5
    assert solution.repeatedNTimes(nums) == expected
