# test_median_of_two_sorted_arrays.py

from median_of_two_sorted_arrays import Solution

solution = Solution()


def test_case_1():
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    assert solution.findMedianSortedArrays(nums1, nums2) == expected


def test_case_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    assert solution.findMedianSortedArrays(nums1, nums2) == expected


def test_custom_case_1():
    nums1 = [1, 3, 8, 9, 15]
    nums2 = [7, 11, 18, 19, 21, 25]
    expected = 11
    assert solution.findMedianSortedArrays(nums1, nums2) == expected


def test_custom_case_2():
    nums1 = [2, 3, 5, 8]
    nums2 = [10, 12, 14, 16, 18, 20]
    expected = 11
    assert solution.findMedianSortedArrays(nums1, nums2) == expected


def test_custom_case_3():
    nums1 = [1, 2]
    nums2 = [3, 6, 9, 18]
    expected = 4.5
    assert solution.findMedianSortedArrays(nums1, nums2) == expected


def test_custom_case_4():
    nums1 = [-6, 4, 7, 11, 14]
    nums2 = [-13, -9, -6, -1, 5, 10]
    expected = 4
    assert solution.findMedianSortedArrays(nums1, nums2) == expected
