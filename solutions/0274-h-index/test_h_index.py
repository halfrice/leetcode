from h_index import Solution

solution = Solution()


def test_case_1():
    citations = [3, 0, 6, 1, 5]
    expected = 3
    assert solution.hIndex(citations) == expected


def test_case_2():
    citations = [1, 3, 1]
    expected = 1
    assert solution.hIndex(citations) == expected
