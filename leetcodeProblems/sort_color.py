"""
    Problem Statement:
        Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
        Note: You are not suppose to use the library's sort function for this problem.
"""
from collections import Counter

class Solution():
    def sortColor(self, color):

        hashmap = Counter(color)
        maxi = max(color)
        color[:] = []

        for i in range(maxi+1):
            color += [i] * hashmap[i]
        
        return color

tc1 = [2,0,2,1,1,0]
print(Solution().sortColor(tc1))