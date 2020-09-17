"""
    Problem Statement:
        Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
        Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
        Could you do this in O(n) runtime?
"""
class Solution():
    def maximumXOR(self, nums):
        trie = {}

        #get the maximum bit length
        max_len_bin = len(bin(max(nums))) - 2
        nums = [[(n >> x) & 1 for x in range(max_len_bin-1, -1, -1)] for n in nums]

        max_xor = 0

        #now create a trie
        for num in nums:
            curr = trie
            xor = trie
            val = 0
            for bit in num:
                if bit not in curr:
                    curr[bit] ={}
                
                #update the node
                curr = curr[bit]

                #xor 
                xor_bit = 1 - bit
                val <<= 1 #left shit

                if xor_bit in xor:
                    xor = xor[xor_bit] #update the xor node
                    val |= 1
                else:
                    xor = xor[bit]

            max_xor = max(max_xor, val)
        
        return max_xor

nums = [2, 5, 3, 10, 25, 8]
nums2 = [3,10,5,2,8]

print(Solution().maximumXOR(nums))
print(Solution().maximumXOR(nums2))