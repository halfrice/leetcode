from min_cost_climbing_stairs import Solution

solution = Solution()


def test_case_1():
    cost = [10, 15, 20]
    expected = 15
    assert solution.minCostClimbingStairs(cost) == expected


def test_case_2():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expected = 6
    assert solution.minCostClimbingStairs(cost) == expected
