"""
    Problem Statement:
        Given a string containing just the characters '(' and ')', find the length of 
        the longest valid (well-formed) parentheses substring.
    
    Input:
        "(()", ")()())", "()(()"
    Output:
        2, 4, 2
"""

def longestParenthesis(string):
        counter = 0 #increase the counter whenever you see valid parameter
        stack = [-1] #initial stack

        if string == None:
            return counter
        
        for num, char in enumerate(string):
            if char == '(':
                stack.append(num)
            else:
                stack.pop()
                if stack:
                    counter = max(counter, num-stack[-1])
                else:
                    stack.append(num)
        
        return counter

tc_1 = ")(((()))))" #8
tc_2 = '(()' #2
tc_3 = "()(()" #2
tc_4 = ')()())' #4
tc_5 = '()(())' #6

print(longestParenthesis(tc_5))
