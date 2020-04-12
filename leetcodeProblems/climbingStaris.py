"""
    Problem Statement:
        You are climbing a stair case. It takes n steps to reach to the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        Note: Given n will be a positive integer.
"""
import functools

def climbing_stairs(n):
    if n == 2 or n == 1:
        return n
    return climbing_stairs(n-2) + climbing_stairs(n-1)

def climbing_stairs_two(n):
    dp = [1] * n
    
    #for step 1 = 1 step required
    dp[0] = 1
    #for step 2 = 2 ways we can reach. 1->1, 2
    dp[1] = 2

    for step in range(2, n):
        #print(step)
        dp[step] = dp[step - 1] + dp[step - 2]
    
    return dp[n-1]

print(climbing_stairs(38))
#print(climbing_stairs_two(38))