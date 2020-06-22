class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        profits = []
        totalsum = 0
        
        while(i < len(prices)):
            buy = prices[i-1]
            sell = prices[i]
            
            profit = sell - buy
            profits.append(profit)
        
            i += 1 #increment
        
        for val in profits:
            if val > 0:
                totalsum += val
        
        return totalsum
