class Solution:
    def productExceptSelf(self, nums):
        left_mul = [] #iterate through lists to store multiplication
        
        for i in range(len(nums)):
            if i == 0:
                left_mul.append(nums[i])
            else:
                left_mul.append(left_mul[i-1] * nums[i])
        
        result = [] #to store results
        
        p = 1
        
        num = len(nums) - 1
        
        while(num >= 0):
            if num == len(nums) - 1:
                result.append(p * left_mul[num-1])
                p *= nums[num]
            elif num == 0:
                result.append(p)
            else:
                result.append(left_mul[num-1] * p)
                p *= nums[num]
                  
            num -= 1
        
        return reversed(result)
