from summary_ranges import Solution

solution = Solution()


def test_case_1():
    nums = [0, 1, 2, 4, 5, 7]
    expected = ['0->2', '4->5', '7']
    assert solution.summaryRanges(nums) == expected


def test_case_2():
    nums = [0, 2, 3, 4, 6, 8, 9]
    expected = ['0', '2->4', '6', '8->9']
    assert solution.summaryRanges(nums) == expected
