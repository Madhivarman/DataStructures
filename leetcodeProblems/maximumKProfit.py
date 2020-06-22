"""
    Problem Statement:
        Say you have an array for which the ith element is the price of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete at most two transactions.
        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock 
        before you buy again).    
"""

class Solution():
    def maximumProfitForAtmostTwoDays(self, prices):
        #formula T[i][j] = max(T[i][j-1], prices[j]-prices[m] + T[i-1][j])
        #where m = 0,1,...,j-1
        maximumProfit = 0
        matrix = [[0 for _ in range(len(prices))] for i in range(2+1)]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                maxval = 0
                for m in range(j):
                    maxval = max(maxval, prices[j]-prices[m]+matrix[i-1][m])
                
                matrix[i][j] = max(matrix[i][j-1], maxval)
        
        #self.printSolution(prices, matrix)
        print(matrix)

        return matrix[-1][-1]
    
    def optimalSolution(self, prices):
        if len(prices) == 0:
            return 0
        
        matrix = [[0 for _ in range(len(prices))] for _ in range(2+1)]

        for i in range(1, len(matrix)):
            max_diff = - prices[0]
            for day in range(1, len(matrix[0])):
                matrix[i][day] = max(matrix[i][day-1],  #no transaction
                                prices[day] + max_diff) #price on that day with maximum diff
                max_diff = max(max_diff, matrix[i-1][day] - prices[day]) #update max_diff

        return matrix[-1][-1]


tc1 = [3,3,5,0,0,3,1,4]
tc2 = [1,2,3,4,5]

print(Solution().optimalSolution(tc1))
print(Solution().optimalSolution(tc2))
