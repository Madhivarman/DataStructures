"""
  Problem Statement:
      You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
      Design an algorithm to find the maximum profit. You may complete at most k transactions.
      Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 1 or k <= 0:
            return 0
        
        profit = 0
        
        if (k >= n//2):
            for i in range(n-1):
                if prices[i] < prices[i+1]:
                    profit += prices[i+1] - prices[i]
            return profit
        
        buy = [-9999] * k
        sell = [0] * k
        
        for i in range(n):
            for j in range(k):
                b = 0 #buy
                if j == 0:
                    b = 0 - prices[i]
                else:
                    b = sell[j-1] - prices[i]
                
                buy[j] = max(b, buy[j])
                sell[j] = max(sell[j], buy[j]+prices[i])
        
        return sell[k-1]
