from daily_temperatures import Solution

solution = Solution()


def test_case_1():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures(temperatures) == expected


def test_case_2():
    temperatures = [30, 40, 50, 60]
    expected = [1, 1, 1, 0]
    assert solution.dailyTemperatures(temperatures) == expected


def test_case_3():
    temperatures = [30, 60, 90]
    expected = [1, 1, 0]
    assert solution.dailyTemperatures(temperatures) == expected
