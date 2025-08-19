from jewels_and_stones import Solution

solution = Solution()


def test_case_1():
    jewels = 'aA'
    stones = 'aAAbbbb'
    expected = 3
    assert solution.numJewelsInStones(jewels, stones) == expected


def test_case_2():
    jewels = 'z'
    stones = 'ZZ'
    expected = 0
    assert solution.numJewelsInStones(jewels, stones) == expected
