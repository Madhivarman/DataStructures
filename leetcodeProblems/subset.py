class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            temp = []
            for r in result:
                temp.append(r + [num])
            
            result += temp
        
        return result


tc1 = [1,2,3]
print(Solution().subsets(tc1))
