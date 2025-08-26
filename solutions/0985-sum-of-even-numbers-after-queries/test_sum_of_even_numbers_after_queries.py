from sum_of_even_numbers_after_queries import Solution

solution = Solution()


def test_case_1():
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    expected = [8, 6, 2, 4]
    assert solution.sumEvenAfterQueries(nums, queries) == expected


def test_case_2():
    nums = [1]
    queries = [[4, 0]]
    expected = [0]
    assert solution.sumEvenAfterQueries(nums, queries) == expected
