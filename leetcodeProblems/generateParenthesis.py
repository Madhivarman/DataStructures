"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
import math

def generateParenthesis(n):
    solution_set = []
    
    def backtrack(string='', left=0, right=0):
        if len(string) == 2 * n:
            solution_set.append(string)
            return
        if left < n:
            backtrack(string + '(', left+1, right)
        if left > right:
            backtrack(string + ')', left, right+1)
    
    backtrack() #call the function
    return solution_set

k = 4
ss = generateParenthesis(k)
print(ss)