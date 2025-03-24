from dota2_senate import Solution

solution = Solution()


def test_case_1():
    senate = 'RD'
    expected = 'Radiant'
    assert solution.predictPartyVictory(senate) == expected


def test_case_2():
    senate = 'RDD'
    expected = 'Dire'
    assert solution.predictPartyVictory(senate) == expected
