from plus_one import Solution

solution = Solution()


def test_case_1():
    digits = [1, 2, 3]
    expected = [1, 2, 4]
    assert solution.plusOne(digits) == expected


def test_case_2():
    digits = [4, 3, 2, 1]
    expected = [4, 3, 2, 2]
    assert solution.plusOne(digits) == expected


def test_case_3():
    digits = [9]
    expected = [1, 0]
    assert solution.plusOne(digits) == expected


def test_case_3():
    digits = [9, 9, 9, 9]
    expected = [1, 0, 0, 0, 0]
    assert solution.plusOne(digits) == expected
