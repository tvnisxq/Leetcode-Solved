class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Brute Force"""
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]

        #         if profit > 0:
        #                 maxProfit = max(maxProfit, profit)
        # return maxProfit

        """ Optimal Approach """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit