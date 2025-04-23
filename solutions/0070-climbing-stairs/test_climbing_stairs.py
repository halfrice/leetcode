from climbing_stairs import Solution

solution = Solution()


def test_case_1():
    n = 2
    expected = 2
    assert solution.climbStairs(n) == expected


def test_case_2():
    n = 3
    expected = 3
    assert solution.climbStairs(n) == expected
