from single_number import Solution

solution = Solution()


def test_case_1():
    nums = [2, 2, 1]
    expected = 1
    assert solution.singleNumber(nums) == expected


def test_case_2():
    nums = [4, 1, 2, 1, 2]
    expected = 4
    assert solution.singleNumber(nums) == expected


def test_case_3():
    nums = [1]
    expected = 1
    assert solution.singleNumber(nums) == expected
