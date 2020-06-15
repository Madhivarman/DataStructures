"""
    Problem Statement:
        Given an array of integers nums and a positive integer k, find whether it's possible to divide 
        this array into k non-empty subsets whose sums are all equal.
"""

class Solution():
    def canPartitionKSubset(self, nums, k):
        if k==0 or sum(nums)%k:
            return False
    
        parts=[0]*k
        t=sum(nums)/k
        
        nums.sort()
        
        if nums[-1]>t:
            return False
        
        def helper(parts,t):
            print(parts, t, nums)

            if not nums:
                #print(parts)
                return True

            v=nums.pop()
            
            for i,p in enumerate(parts):
                if p+v<=t:
                    parts[i]+=v
                    if helper(parts,t):
                        return True
                    
                    print("inner loop:{},{}".format(i, parts))
                    parts[i]-=v
                    if not p:
                        break
                        
            nums.append(v)
            return False
    
    
        return helper(parts,t)


tc1, tc1_k = [4, 3, 2, 3, 5, 2, 1], 4 
tc2, tc2_k = [1, 1, 3, 2, 2], 4
tc3, tc3_k = [10,10,10,7,7,7,7,7,7,6,6,6], 3

print(Solution().canPartitionKSubset(tc1, tc1_k))
print(Solution().canPartitionKSubset(tc2, tc2_k))
print(Solution().canPartitionKSubset(tc3, tc3_k))