from best_time_to_buy_and_sell_stock_ii import Solution

solution = Solution()


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    expected = 7
    assert solution.maxProfit(prices) == expected


def test_case_2():
    prices = [1, 2, 3, 4, 5]
    expected = 4
    assert solution.maxProfit(prices) == expected


def test_case_3():
    prices = [7, 6, 4, 3, 1]
    expected = 0
    assert solution.maxProfit(prices) == expected
