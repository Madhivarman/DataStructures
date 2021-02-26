"""
    Problem Statement:
        Given two sequences pushed and popped with distinct values, return true if and only if 
        this could have been the result of a sequence of push and pop operations on an initially 
        empty stack.
"""

class Solution:
    #logic 2
    def logic_2(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_ptr = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[pop_ptr]:
                stack.pop()
                pop_ptr += 1
        
        return pop_ptr == len(popped)
                
    #logic 1
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_ptr = 0
        pop_ptr = 0
        length = len(pushed)
        stack = []
        
        while(push_ptr < length or pop_ptr < length):
            if pop_ptr < length and stack and stack[-1] == popped[pop_ptr]:
                stack.pop()
                pop_ptr += 1
            elif push_ptr < length:
                stack.append(pushed[push_ptr])
                push_ptr += 1
            else:
                return False
        
        return True
