class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                substring_one = s[left:right]
                substring_two = s[left+1:right+1]
                return substring_one==substring_one[::-1] or substring_two==substring_two[::-1]
            
        return True