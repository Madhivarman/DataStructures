"""
    Problem Statement:
        Given an unsorted array of integers, find the length of longest increasing subsequence.
"""

class Solution():
    def lengthOfLIS(self, nums):
        output = 0
        subseq_len = [] #to store length

        #iterate through the nums
        for num, i in enumerate(nums):
            maxlen = 1

            for j in range(0, num):
                #condition
                if i > nums[j]:
                    curr_len = subseq_len[j] + 1 #update the current length

                    #check for max
                    if curr_len > maxlen:
                        maxlen = curr_len

            subseq_len.append(maxlen)

            if maxlen > output:
                output = maxlen

        return output

tc1 = [10,9,2,5,3,7,101,18]
tc2 = [2,3,4,5,6,6,5,6,7,8,60,61,62,63]
tc3 = [10,9,2,5,3,7,101,18,19,20]

print(Solution().lengthOfLIS(tc1))
print(Solution().lengthOfLIS(tc2))
print(Solution().lengthOfLIS(tc3))
