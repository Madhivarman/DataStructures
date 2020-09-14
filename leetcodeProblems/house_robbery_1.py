"""
  Problem Statement:
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
        the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
        it will automatically contact the police if two adjacent houses were broken into on the same night.
        
        Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount 
        of money you can rob tonight without alerting the police.
"""

class Solution:
    
    def maximumProfit(self, chances):
        #robbing first house, chances = [2,3,2]
        if(len(chances) == 0):return 0
        if(len(chances) == 1):return chances[0]

        dp = [chances[0], max(chances[0], chances[1])] #dp=[2,3]

        for i in range(2, len(chances)):
            maxval = max(dp[i-2] + chances[i], dp[i-1])
            dp.append(maxval)

        return dp[-1] #return the maximum state
    
    def rob(self, house: List[int]) -> int:
        maximumAmount = 0
        if(len(house) == 0):return 0
        if(len(house) == 1):return house[0]
        
        #consider robbing the first house
        robbingFirstHouse = house[:len(house)]
        robbingLastHouse = house[1:]
        
        #check what is the maximum profit
        t1 = self.maximumProfit(robbingFirstHouse)
        t2 = self.maximumProfit(robbingLastHouse)

        maximumAmount = max(t1, t2)
        return maximumAmount
