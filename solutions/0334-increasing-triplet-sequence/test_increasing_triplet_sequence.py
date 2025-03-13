from increasing_triplet_sequence import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4, 5]
    expected = True
    assert solution.increasingTriplet(nums) == expected


def test_case_2():
    nums = [5, 4, 3, 2, 1]
    expected = False
    assert solution.increasingTriplet(nums) == expected


def test_case_3():
    nums = [2, 1, 5, 0, 4, 6]
    expected = True
    assert solution.increasingTriplet(nums) == expected
