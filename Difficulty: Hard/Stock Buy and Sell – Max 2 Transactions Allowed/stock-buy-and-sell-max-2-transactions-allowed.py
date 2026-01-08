class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
            
        # profit1[i] stores max profit with one transaction from day 0 to i
        profit1 = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            profit1[i] = max(profit1[i-1], prices[i] - min_price)
            
        # profit2[i] stores max profit with one transaction from day i to n-1
        profit2 = [0] * n
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            profit2[i] = max(profit2[i+1], max_price - prices[i])
            
        # The maximum profit will be the max of profit1[i] + profit2[i]
        max_total_profit = 0
        for i in range(n):
            max_total_profit = max(max_total_profit, profit1[i] + profit2[i])
            
        return max_total_profit