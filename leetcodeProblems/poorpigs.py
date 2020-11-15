"""
    Problem Statement:
        There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. 
        They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum 
        amount of pigs you need to figure out which bucket is poisonous within one hour?

        Answer this question, and write an algorithm for the general case.

        General case:
        If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x)
        you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.
"""
class Solution():
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        tests = (minutesToTest / minutesToDie)  + 1
        while(tests**pigs < buckets):
            pigs += 1
        return pigs

tc1 = (1000, 15, 60)
print(Solution().poorPigs(tc1[0], tc1[1], tc1[2]))