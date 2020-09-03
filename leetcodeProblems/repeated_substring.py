class Solution:
    def repeatedSubstringPattern(self, s):
        string_ = ""
        
        #iterate till the middle
        for i in range(len(s)//2):
            string_ += s[i] #add the string
            
            if len(s) % len(string_) == 0:
                if string_ * (len(s) // len(string_)) == s:
                    return True
                
        return False

tc1 = "abab" #True
tc2 = "aba" #False
tc3 = "abcabcabc" #True

print(Solution().repeatedSubstringPattern(tc1))
print(Solution().repeatedSubstringPattern(tc2))
print(Solution().repeatedSubstringPattern(tc3))
