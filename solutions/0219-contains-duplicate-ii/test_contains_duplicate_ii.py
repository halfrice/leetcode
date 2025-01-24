from contains_duplicate_ii import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 1]
    k = 3
    expected = True
    assert solution.containsNearbyDuplicate(nums, k) == expected


def test_case_2():
    nums = [1, 0, 1, 1]
    k = 1
    expected = True
    assert solution.containsNearbyDuplicate(nums, k) == expected


def test_case_3():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    expected = False
    assert solution.containsNearbyDuplicate(nums, k) == expected
