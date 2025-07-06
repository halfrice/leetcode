from largest_rectangle_in_histogram import Solution

solution = Solution()


def test_case_1():
    heights = [2, 1, 5, 6, 2, 3]
    expected = 10
    assert solution.largestRectangleArea(heights) == expected


def test_case_2():
    heights = [2, 4]
    expected = 4
    assert solution.largestRectangleArea(heights) == expected
