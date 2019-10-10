"""
        Two key observations in the problem:
            1. A decreasing array is the last permutation of the array, and the 
               next one is the reverse of it. For example, `3,2,1` is the last 
               permutation of this array and `1,2,3` will be next.
            2. For a decreasing subarray, there is a number right before the 
               subarray that "leads" the subarray, e.g., `2,4,3,1` in which `2` 
               "leads" the subarray `4,3,1`. Similarly, the decreasing subarray 
               is the last permutation of itself, and the next one should be 
               mostly the reverse of the subarray, except that the "leading" 
               number is going to change. Looking at the previous example, the 
               next permutation is `3,1,2,4` wherein the "leading" number is 
               `3`, which is the next greater number than `2` in the sequence. 
               Herein, the rule for generating the next permutation for a 
               subarray is - 1) swap the "leading" number and the next greater 
               one in the decreasing subarray; 2) reverse the decreasing 
               subarray.
        In summary, the whole process should be the following:
            1. Find the decreasing subarray if not the entire array
            2. If it is not the entire array, swap the "leading" number and its 
               next greater number in the decreasing subarray
            3. Reverse the decreasing part
           
        Note:
          Description and solution credit goes to solution provider on Leetcode
"""
def nextPerumute(nums):
    
    length = len(nums)
    if length == 1:
        return
    
    i = length - 2
    # find the decreasing the subarray
    while i > 0:
        if nums[i] < nums[i+1]:
            break
        i -= 1
    
    if i == 0 and nums[i] >= nums[i+1]:
        s, e = 0, length - 1
    else:
        cur = i 
        while i < length - 1 and nums[cur] < nums[cur+1]:
            i += 1
        
        nums[cur], nums[i] = nums[i], nums[cur]

        #the decreasing subarray will be reversed
        s, e = cur + 1, length - 1

    while s < e:
        nums[s], nums[e] = nums[e], nums[s]
        s += 1
        e -= 1
    
    return nums


nextPoss = nextPerumute([1,4,3,2])
print(nextPoss)
    
