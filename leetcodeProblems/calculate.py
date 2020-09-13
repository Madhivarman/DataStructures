"""
    Problem Statement:
        Implement a basic calculator to evaluate a simple expression string.
        The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
        non-negative integers and empty spaces .
"""

class Solution():
    def calculate(self, expression):
        #remove unncessary space
        expression = "".join(expression.split(" "))

        def dfs(s, i):
            #tmp to maintain the index
            #ops to keep track the operations
            #stack_num to keep track values
            tmp, ops, stack_num = '','',[]
            
            while(i < len(s)):
                char = s[i]

                if char == '(':
                    #call the dfs function recursively to
                    #calculate the result enclose in the bracket
                    tmp, go_head = dfs(s, i+1)
                    i = go_head
                
                elif char == ')':
                    #closing brack encountered, return the current answer and index
                    if len(stack_num) == 0:
                        return int(tmp), i
                    else:
                        #valid if we have encountered the value before
                        if ops == '+':
                            return (stack_num.pop() + int(tmp)), i
                        else:
                            return (stack_num.pop() - int(tmp)), i
                
                elif char in ['+', '-']:
                    if len(stack_num) == 0:
                        stack_num.append(int(tmp))
                    else:
                        if ops == '+':
                            stack_num.append(stack_num.pop() + int(tmp))
                        else:
                            stack_num.append(stack_num.pop() - int(tmp))
                    
                    ops = char
                    tmp = '' #initialize the temp

                else:
                    tmp += char
                
                i += 1 #increment the index
        
            #edge cases
            if len(stack_num) == 0:
                return int(tmp)
            else:
                if ops == '+':
                    return stack_num.pop() + int(tmp)
                else:
                    return stack_num.pop() + int(tmp)
        
        #params - (expression, index)
        return dfs(expression, 0)


tc1 = "1+1" #2
tc2 = "2-1+1" #2
tc3 = "(1+(4+5+2)-3)+(6+8)" #23

print(Solution().calculate(tc1))
print(Solution().calculate(tc2))
print(Solution().calculate(tc3))