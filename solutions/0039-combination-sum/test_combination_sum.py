from combination_sum import Solution

solution = Solution()


def test_case_1():
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    assert solution.combinationSum(candidates, target).sort() == expected.sort()


def test_case_2():
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert solution.combinationSum(candidates, target).sort() == expected.sort()


def test_case_3():
    candidates = [2]
    target = 1
    expected = []
    assert solution.combinationSum(candidates, target).sort() == expected.sort()


def test_case_4():
    candidates = [8, 7, 4, 3]
    target = 11
    expected = [[8, 3], [7, 4], [4, 4, 3]]
    assert solution.combinationSum(candidates, target).sort() == expected.sort()
