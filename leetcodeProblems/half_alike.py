"""
  Problem Statement:
      You are given a string s of even length. Split this string into two halves of equal lengths, 
      and let a be the first half and b be the second half.

      Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
      Notice that s contains uppercase and lowercase letters.

      Return true if a and b are alike. Otherwise, return false.
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def countVowels(temp, vowels):
            count = 0
            for char in temp:
                if char in vowels:
                    count += 1
            return count
        
        vowels = ['a','e','i','o','u']
        s = s.lower() #convert into lower
        midpoint = len(s) // 2
        fh, sh = s[:midpoint], s[midpoint:] #first half, second half
        
        fhc = countVowels(fh, vowels)
        shc = countVowels(sh, vowels)
        
        return fhc == shc
