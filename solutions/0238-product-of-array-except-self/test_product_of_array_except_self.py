from product_of_array_except_self import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected


def test_case_2():
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums) == expected


def test_custom_case_1():
    nums = [2, 4, 5, 9]
    expected = [180, 90, 72, 40]
    assert solution.productExceptSelf(nums) == expected
