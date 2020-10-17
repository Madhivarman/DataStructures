"""
  Problem Statement:
    All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When 
    studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
    Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
"""
class Solution:
    def findRepeatedDnaSequences(self, s):
        #using window method find if the DNA
        #sequence has repeated outside of the window
        result = []
        subseq_map = defaultdict(int)
        
        for i in range(len(s)):
            substring = s[i : i+10]
            if substring in subseq_map:
                subseq_map[substring] += 1
            else:
                subseq_map[substring] = 1
        
        for k,v in subseq_map.items():
            if v >= 2:
                result.append(k)
        
        return result
