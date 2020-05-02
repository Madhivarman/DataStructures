"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character may map to itself.
"""

class Solution():
    def isIsomorphic(self, s, t):        
        mappings = {} #mappings
        ismorphic = True

        #helper functions
        def isalreadyMapped(source, target):
            bool_ = False
            if(target in mappings.values()):
                bool_ = True
            
            return bool_
        
        def isMappedcorrect(source, target):
            if(mappings[source] == target):
                return True
            else:
                return False

        
        #length mismatch
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            if s[i] not in mappings:
                if(isalreadyMapped(s[i], t[i])):
                    return False
                else:
                    mappings[s[i]] = t[i]
            else:
                if(isMappedcorrect(s[i], t[i])):
                    continue
                else:
                    return False


        return ismorphic

a = "paper"
b = "titrr"

print(Solution().isIsomorphic(a, b))