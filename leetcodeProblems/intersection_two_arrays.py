"""
  Problem Statement:
      Given two arrays, write a function to compute their intersection
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A_dict, B_dict = defaultdict(int), defaultdict(int)
        result = []
        q = deque([])
        
        for i in nums1:
            A_dict[i] += 1
        
        for i in nums2:
            B_dict[i] += 1
        
        common = list(set(nums1).intersection(nums2))
        
        for i in common:
            if i in A_dict and i in B_dict and A_dict[i] > 0 and B_dict[i] > 0:
                result.append(i)
                A_dict[i] -= 1
                B_dict[i] -= 1
                common.extend([i for m in range(A_dict[i] + B_dict[i])])
                
        return result
