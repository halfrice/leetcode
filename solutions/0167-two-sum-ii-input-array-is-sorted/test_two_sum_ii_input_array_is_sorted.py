from two_sum_ii_input_array_is_sorted import Solution

solution = Solution()


def test_case_1():
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected


def test_case_2():
    numbers = [2, 3, 4]
    target = 6
    expected = [1, 3]
    assert solution.twoSum(numbers, target) == expected


def test_case_3():
    numbers = [-1, 0]
    target = -1
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected
