# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 1
        profit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
            j += 1

        return profit
