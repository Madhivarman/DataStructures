"""
    Problem Statement:
        Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
        find the area of largest rectangle in the histogram.
"""
class Solution():
    def largestRectangeSum(self, histogram):
        maxarea = 0
        #stack to keeping tracking
        stack = []
        index = 0 #pointer to find where are we 

        while (index < len(histogram)):
            #if the stack is empty or current index hieght us greater
            #than the previous index hieght just push it to the stack
            if len(stack) == 0 or histogram[stack[-1]] <= histogram[index]:
                stack.append(index)
                index += 1
                print(stack, index)
            else:
                #remove from the top of the stack
                top_of_stack = stack.pop()
                if stack:
                    area = histogram[top_of_stack] * (index - stack[-1] - 1)
                else:
                    area = histogram[top_of_stack] * index
    
                # update max area, if needed 
                maxarea = max(maxarea, area) 
        
        #while the stack is still not empty
        while(stack):
            top_of_stack = stack.pop()
            if stack:
                area = histogram[top_of_stack] * (index - stack[-1]- 1)
            else:
                area = histogram[top_of_stack] * index
            maxarea = max(maxarea, area)

        return maxarea

tc1 = [2, 1, 5, 6, 2, 3]
tc2 = [2, 1, 5, 6, 12, 3]

#print(Solution().largestRectangeSum(tc1))
print(Solution().largestRectangeSum(tc2))