class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        #return empty lists
        if not nums:
            return [[]]
        
        for index, pointer in enumerate(nums):
            #calculate the values before and after the current
            #index
            remaining = nums[:index] + nums[index+1:]
            #recursion calling
            tmp_permutation = self.permute(remaining)
            
            for permutation in tmp_permutation:
                permutation.insert(0, pointer)
            
            result.extend(tmp_permutation)
        
        
        return result
