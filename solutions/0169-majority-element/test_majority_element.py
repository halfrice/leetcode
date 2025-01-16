from majority_element import Solution

solution = Solution()


def test_case_1():
    n = [3, 2, 3]
    expected = 3
    assert solution.majorityElement(n) == expected


def test_case_2():
    n = [2, 2, 1, 1, 1, 2, 2]
    expected = 2
    assert solution.majorityElement(n) == expected
