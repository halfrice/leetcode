from maximum_difference_between_adjacent_elements_in_a_circular_array import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 4]
    expected = 3
    assert solution.maxAdjacentDistance(nums) == expected


def test_case_2():
    nums = [-5, -10, -5]
    expected = 5
    assert solution.maxAdjacentDistance(nums) == expected


def test_case_3():
    nums = [1, -2, 3, -4, 5, -6]
    expected = 11
    assert solution.maxAdjacentDistance(nums) == expected
