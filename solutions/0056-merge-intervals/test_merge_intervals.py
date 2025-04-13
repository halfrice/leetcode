from merge_intervals import Solution

solution = Solution()


def test_case_1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert solution.merge(intervals) == expected


def test_case_2():
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    assert solution.merge(intervals) == expected
