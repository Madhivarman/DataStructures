"""
  Problem Statement:
    Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
    Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].
"""
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        R = int(right)
        L = int(left)
        
        sqrt_sp = ["11","22"]
        
        for i in sqrt_sp:
            for j in ['0','1','2']:
                sqrt_sp.append(i[:len(i)//2] + j + i[len(i)//2:])
                
            if int(i) ** 2 > R:
                break
        
        sqrt_sp += ['1','2','3']
        ans = 0
        
        for i in sqrt_sp:
            s = int(i) ** 2
            if L <= s <= R and str(s) == str(s)[::-1]:
                ans += 1
        return ans
