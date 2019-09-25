"""
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.
"""
def removeDuplicates(nums):
    seen = set()
    count = 0
    for i in nums:
        if i not in seen:
            nums[count] = i
            count += 1
            
        seen.add(i)
        
    return count

aslist = [1,1,1,2,2,3,4,5,5,6]
solution = removeDuplicates(aslist)

print(solution)