"""
    Problem Statement:
        Given 2 strings X and Y. Write a program to find the smallest subset in the string X
        that contains all the characters in Y. If characters in Y are not found in X, print -1.
        Example:
            1.
                Input:
                X = PHONE
                Y = HEN
                Output:
                HONE
            2.
                Input:
                X = ZOHOCORPORATION
                Y = PCO
                Output:
                CORP
            3.
                Input:
                X = ZOHOCORPORATION
                Y = ONR
                Output:
                RATION
"""
from collections import defaultdict
import itertools

class Solution():
    def findSubstring(self, S, P):

        if len(list(set(P).intersection(S))) != len(P):
            return "-1"

        #using 2 pointer approach
        start, end = 0, len(S) // 2
        result = 9999
        tf_s, tf_e = 0, end

        while(end < len(S)):
            substring = S[start: end+1]
            set_ = list(set(P).intersection(substring))
            if len(set_) == len(P) and start < end:
                # print("{},{}=>{},{}".format(start, end, substring, set_))
                l = len(substring)
                if l < result:
                    tf_s, tf_e = start, end
                    result = l #update the result
                    start += 1 #update the start

            else:
                end += 1 #update the end
        
        return S[tf_s:tf_e+1]



tc1_X, tc1_Y = "PHONE", "HEN"
tc2_X, tc2_Y = "MADHIVARMAN", "NZM"
tc3_X, tc3_Y = "ZOHOCORPORATION", "PCO"
tc4_X, tc4_Y = "ZOHOCORPORATION", "ONR"
tc5_X, tc5_Y = "ZOHOCORPORATION", "APRO"

print(Solution().findSubstring(tc1_X, tc1_Y))
print(Solution().findSubstring(tc2_X, tc2_Y))
print(Solution().findSubstring(tc3_X, tc3_Y))
print(Solution().findSubstring(tc4_X, tc4_Y))
print(Solution().findSubstring(tc5_X, tc5_Y))