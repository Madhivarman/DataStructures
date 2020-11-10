"""
    Problem Statement:
        Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) 
        under the following rules:
        Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
        Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
"""
import itertools
from collections import Counter
class Solution():
    def numTriplets(self, nums1, nums2):
        nums1_comb = Counter([v1 * v2 for v1, v2 in itertools.combinations(nums1, 2)])
        nums2_comb = Counter([v1 * v2 for v1, v2 in itertools.combinations(nums2, 2)])
        return sum([nums2_comb[n**2] for n in nums1]) + sum([nums1_comb[n**2] for n in nums2])

tc1_nums1, tc1_nums2 = [7,4], [5,2,8,9]
tc2_nums1, tc2_nums2 = [1,1], [1,1,1]
tc3_nums1, tc3_nums2 = [7,7,8,3], [1,2,9,7]

print(Solution().numTriplets(tc1_nums1, tc1_nums2))
print(Solution().numTriplets(tc2_nums1, tc2_nums2))
print(Solution().numTriplets(tc3_nums1, tc3_nums2))