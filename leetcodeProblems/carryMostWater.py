"""
    Problem Statement:
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

def maxCapacityContainer(containers):

    #assign zero as default to both left and right containers
    left, right, volume = 0,len(containers)-1, 0
    
    #iterate through the range
    for i in range(len(containers)):
        
        leftBar, rightBar = containers[left], containers[right]
        volume = max(volume, min(leftBar, rightBar) * (right - left))

        if left == right:
            return volume

        if leftBar < rightBar:
            left += 1
        else:
            right -= 1


capacity = maxCapacityContainer([1,8,6,2,5,4,8,3,7])
print("Maximum capacity holds:{}".format(capacity))