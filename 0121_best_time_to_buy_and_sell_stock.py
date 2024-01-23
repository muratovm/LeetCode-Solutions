class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0
        for price in prices:
            start = min(price, start)
            profit = max(profit, price - start)
        return profit
