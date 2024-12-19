from top_k_frequent_elements import Solution

solution = Solution()


def test_case_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    assert solution.topKFrequent(nums, k) == expected


def test_case_2():
    nums = [1]
    k = 1
    expected = [1]
    assert solution.topKFrequent(nums, k) == expected
