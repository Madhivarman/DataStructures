"""
	Problem Statement:
		Given an array of citations (each citation is a non-negative integer) of a 
		researcher, write a function to compute the researcher's h-index.
		According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her 
		N papers have at least h citations each, and the other N − h papers have no more than h citations each."
"""

class Solution:
    def hIndex(self, citations):
        citations.sort()
        hindex = 0
        
        for idx, val in enumerate(citations):
            if val >= (len(citations) - idx):
                hindex = max(hindex, len(citations)-idx)
        
        return hindex
	
    def withoutsorting(self, citations):
        hindex = 0
        #safe check
        if len(citations) == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0

        def helper(i):
            bool_ =  False
            atleast_iterations = 0

            for m in citations:
                if atleast_iterations == i:
                    bool_ = True
                    return bool_
                if m >= i:
                    atleast_iterations += 1
            
            if atleast_iterations == i:
                return True
            
            return bool_
        
        num = 1
        for i in citations:   
            if i == 0:
                pass

            elif helper(num):
                hindex = max(num, hindex)

            else:
                pass
            
            num += 1

        return hindex
