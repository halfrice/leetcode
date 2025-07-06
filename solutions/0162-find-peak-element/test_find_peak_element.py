from find_peak_element import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 1]
    expected = 2
    assert solution.findPeakElement(nums) == expected


def test_case_2():
    nums = [1, 2, 1, 3, 5, 6, 4]
    expected = 5
    assert solution.findPeakElement(nums) == expected


def test_case_3():
    nums = [1, 2, 3, 4]
    expected = 3
    assert solution.findPeakElement(nums) == expected
