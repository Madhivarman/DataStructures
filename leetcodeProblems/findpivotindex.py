"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

def search(aslist, target):
    pivot_index = -1
    """
        the idea of the problem is to reduce the iteration in the list.
        The first thing is to decide whether we need to traverse from the
        start or from the end. 
    """
    N = len(aslist)
    
    if target > aslist[-1]:
        i = 1
        #return if the first element is the target
        if target == aslist[0]:
            return 0

        #start iterating through the list
        while(i < len(aslist)):
            #if the condition doesn't follow the question
            #just return -1
            if aslist[i] >= aslist[i-1] and aslist[i] < target:
                i += 1
            elif aslist[i] == target:
                return i
            else:
                break
    
    else:

        if target == aslist[-1]:
            return len(aslist) - 1
        
        i = len(aslist) - 2

        while(i>=0):
            if aslist[i] >= aslist[i-1] and aslist[i] > target:
                i -= 1
            elif aslist[i] == target:
                return i
            else:
                break
    
    
    return pivot_index


pivot_list = [4,5,6,7,0,1,2]
ts_1 = [32,44,55,66,72,0,2,6,7,8,9]
target = 2

print(search(ts_1, target))
