from insert_interval import Solution

solution = Solution()


def test_case_1():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    expected = [[1, 5], [6, 9]]
    assert solution.insert(intervals, newInterval) == expected


def test_case_2():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    expected = [[1, 2], [3, 10], [12, 16]]
    assert solution.insert(intervals, newInterval) == expected
