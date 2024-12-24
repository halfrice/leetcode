from best_time_to_buy_and_sell_stock import Solution

solution = Solution()


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    assert solution.maxProfit(prices) == expected


def test_case_2():
    prices = [7, 6, 4, 3, 1]
    expected = 0
    assert solution.maxProfit(prices) == expected


def test_custom_case_1():
    prices = [4, 1, 5, 2, 7]
    expected = 6
    assert solution.maxProfit(prices) == expected


def test_custom_case_2():
    prices = [2, 4, 1]
    expected = 2
    assert solution.maxProfit(prices) == expected


def test_custom_case_3():
    prices = [3, 2, 6, 5, 0, 3]
    expected = 4
    assert solution.maxProfit(prices) == expected
