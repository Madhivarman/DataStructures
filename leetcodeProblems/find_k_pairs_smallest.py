"""
  Problem Statement:
      You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
      Define a pair (u,v) which consists of one element from the first array and one element from the second array.
      Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [] #idea is to use minimum heap
        #iterate
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                #base condition
                if len(min_heap) < k:
                    heappush(min_heap, (-nums1[i]-nums2[j], i, j))
                else:
                    #check if the last element is lesser
                    #then the current addup
                    if nums1[i] + nums2[j] > -min_heap[0][0]:
                        break
                    else:
                        heappop(min_heap)
                        heappush(min_heap, (-nums1[i]-nums2[j], i, j))
        
        result = []
        
        while k and min_heap:
            nums, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1 #decrement wise
        
        return result
