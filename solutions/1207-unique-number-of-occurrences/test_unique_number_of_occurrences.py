from unique_number_of_occurrences import Solution

solution = Solution()


def test_case_1():
    arr = [1, 2, 2, 1, 1, 3]
    expected = True
    assert solution.uniqueOccurrences(arr) == expected


def test_case_2():
    arr = [1, 2]
    expected = False
    assert solution.uniqueOccurrences(arr) == expected


def test_case_3():
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    expected = True
    assert solution.uniqueOccurrences(arr) == expected
