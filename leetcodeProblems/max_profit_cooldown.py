"""
  Problem Statement:
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times)
    with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""
class Solution():
  def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        n = len(prices)
        diff = [prices[x+1] - prices[x] for x in range(n-1)]
        
        dp, dp_max = [0] *(n+1), [0] *(n+1)
        
        #iterate through the list
        for i in range(n-1):
            #skip 2 elements and take dp[i-3] (or) do not
            #take any elements, just carry forward
            dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
            
            #maximum of current profit (or) previous profit
            dp_max[i] = max(dp[i], dp_max[i-1])
        
        #print(diff, dp_max)
        return dp_max[-3]
