"""
    Problem Statement:
        Given a string S and a string T, find the minimum window in S which will contain all the characters in T
        in complexity O(n).
"""
import collections

class Solution():

    def minimumWindowSubString(self, s, t):
        # t_cnts as look-up of t
        t_cnts = collections.Counter(t)
        
        # slow := the opening of window
        # start := the start index of final result
        # parts := the cumlated valid parts need to be used to compose t
        slow = start = parts = 0
        minlen = float('inf')
        
        # fast is the end of window
        for fast in range(len(s)):
            # if current char is in t, decrease the counts in t_cnts
            # check if t_cnts[s[fast]] >= 0,
            # if so means thr prior decrease is a valid part that should be included in ans
            if s[fast] in t_cnts:
                t_cnts[s[fast]] -= 1
                if t_cnts[s[fast]] >= 0:
                    parts += 1
            

            # Since valid parts are fullfilled
            # Update ans, and adjust window size exploring alternatives by moving forward slow
            while parts == len(t):
                if minlen > fast - slow + 1:
                    minlen = fast - slow + 1
                    start = slow
                    #print("Minimum Length:{}, start:{}, slow:{}, parts:{}".format(minlen, start, slow, parts))
                # if current char is in t, add back to t_cnts
                # check if t_cnts[s[slow]] > 0
                # which means the prior valid parts have been removed
                # thereby, parts -= 1
                if s[slow] in t_cnts:
                    t_cnts[s[slow]] += 1
                    if t_cnts[s[slow]] > 0:
                        parts -= 1
                slow += 1


        return s[start : (start + minlen)] if minlen != float('inf') else ""


tc1_S = "ADOBECODEBANC"
tc1_T = "ABC"

tc2_S = "AZJSKFZSTS"
tc2_T = "SZ"

tc3_S = "MADHIVARMAN"
tc3_T = "xyz"

tc4_S = "ab"
tc4_T = "a"

tc5_S = "abc"
tc5_T = "ac"

print(Solution().minimumWindowSubString(tc1_S, tc1_T))
print(Solution().minimumWindowSubString(tc2_S, tc2_T))
print(Solution().minimumWindowSubString(tc3_S, tc3_T))
print(Solution().minimumWindowSubString(tc4_S, tc4_T))
print(Solution().minimumWindowSubString(tc5_S, tc5_T))