from combination_sum_ii import Solution

solution = Solution()


def test_case_1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert solution.combinationSum2(candidates, target).sort() == expected.sort()


def test_case_2():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    expected = [[1, 2, 2], [5]]
    assert solution.combinationSum2(candidates, target).sort() == expected.sort()
