"""
  Problem Statement:
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means the expression would always \
    evaluate to a result, and there will not be any division by zero operation.
"""
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ["*", "/", "+", "-"]
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,  # use operator.div for Python 2
            '%' : operator.mod,
            '^' : operator.xor
        }
        
        for token in tokens:
            if token not in symbols:
                stack.append(token)
            elif str(token) in symbols:
                b = stack.pop() #get last two
                a = stack.pop()
                result = ops[token](int(a), int(b))
                stack.append(int(result))
        
        return stack[-1]
