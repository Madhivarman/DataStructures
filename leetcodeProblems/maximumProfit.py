"""
    Problem Statement:
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
        design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.
"""
class Solution():
    def maximumProfit(self, priceStock):
        maximumProfit = 0

        for num, i in enumerate(priceStock):
            #sort the subwindow
            subwindow = sorted(priceStock[num:])

            if subwindow[-1] > i:
                profit = subwindow[-1] - i
                maximumProfit = max(profit, maximumProfit)
        
        return maximumProfit
    
    def optimalSolution(self, priceStock):
        i, j = 0, 1
        maxprofit = 0

        while True:
            if j >= len(priceStock):
                break

            buy = priceStock[i]
            sell = priceStock[j]
            
            if sell > buy:
                profit = sell - buy
                maxprofit = max(profit, maxprofit)
                j += 1
            
            if buy >= sell:
                i += 1
                j = i + 1
        
        return maxprofit
            


tc1 = [7,1,5,3,6,4]
tc2 = [7,6,4,3,1]
tc3 = [7,6,4,3,1,10, 15, 2, 6, 7, 70]

print(Solution().maximumProfit(tc1))
print(Solution().maximumProfit(tc2))
print(Solution().maximumProfit(tc3))
