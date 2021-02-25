"""
  Problem Statement:
    Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for char in S:
            if char == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max( val * 2, 1)
        
        return stack[-1]
      
tc1 = "(())"
print(Solution().scoreOfParentheses(tc1))
