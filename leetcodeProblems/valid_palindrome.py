"""
  Given a string check if the string is a valid palindrom (or) not
"""

class Solution:
    def isPalindrome(self, s):        
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        i = 0
        j = len(s) - 1
        
        while(i <= j):
            char_left = s[i]
            char_right = s[j]
            if char_left == char_right:
                i += 1
                j -= 1
            else:
                return False
        
        return True
