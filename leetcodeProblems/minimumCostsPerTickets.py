"""
  In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

  Train tickets are sold in 3 different ways:

  a 1-day pass is sold for costs[0] dollars;
  a 7-day pass is sold for costs[1] dollars;
  a 30-day pass is sold for costs[2] dollars.
  The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

  Return the minimum number of dollars you need to travel every day in the given list of days.
"""

from collections import Counter

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1] 
        day = Counter(days)
        dp = [0 for x in range(last_day+1)]
        
        
        for i in range(last_day+1):
            if i not in day:
                dp[i] = dp[i-1]
            else:
                one = dp[max(0, i-1)] + costs[0]
                seven = dp[max(0, i-7)] + costs[1]
                thirty = dp[max(0, i - 30)] + costs[2]
                
                dp[i] = min(one, seven, thirty)
        
        return dp[-1]
