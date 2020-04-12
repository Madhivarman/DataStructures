class Solution:
    def plus_one(self, nums):        
        result = ''
        
        if len(nums) == 0:
            return [1]
        
        if len(nums) == 1:
            for x in nums:
                result = x + 1
                result = str(result)
        else:
            p = len(nums) - 1
            carry = 0

            while(p >= 0):
                
                #first condition
                if p == len(nums) - 1:
                    val = nums[p] + 1 + carry
                else:
                    val = nums[p] + carry
                    
                #carry condition
                if val > 9:
                    carry = int(str(val)[0])
                    result = str(val)[-1] + result
                else:
                    result = str(val) + result
                    carry = 0
                
                #final condition
                if p == 0 and carry != 0:
                    result = str(carry) + result

                p -= 1 #update the pointer
        
        return [int(x) for x in result]

tc1 = [1,2,3]
tc2 = [4,3,2,1]
tc3 = [0,0,0,0,0,1]
tc4 = []
tc5 = [1,2,3,9]
tc6 = [1,9,0,8,7,5,0]

print(Solution().plus_one(tc1))
print(Solution().plus_one(tc2))
print(Solution().plus_one(tc3))
print(Solution().plus_one(tc4))
print(Solution().plus_one(tc5))
print(Solution().plus_one(tc6))