from merge_sorted_array import Solution

solution = Solution()


def test_case_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    expected = [1, 2, 2, 3, 5, 6]
    assert nums1 == expected


def test_case_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected


def test_case_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected
