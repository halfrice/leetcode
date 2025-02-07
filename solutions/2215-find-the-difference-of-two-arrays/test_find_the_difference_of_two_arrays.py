from find_the_difference_of_two_arrays import Solution

solution = Solution()


def test_case_1():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    expected = [[1, 3], [4, 6]]
    assert solution.findDifference(nums1, nums2) == expected


def test_case_2():
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    expected = [[3], []]
    assert solution.findDifference(nums1, nums2) == expected
