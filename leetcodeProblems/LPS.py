def longestPalindrome(s):
        
        #return if length=1
        if len(s) <= 1:
            return s
        
        start=0
        end=0 # to keep track of the boundaries
        
        for i in range(len(s)):
            max1 = self.get_max_len(s, i, i+1, len(s))
            max2 = self.get_max_len(s, i, i, len(s))
            maxlen = max(max1, max2)
            
            if maxlen > end-start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        
        return s[start:end+1]
            
    
    def get_max_len(self, s, left, right, length):
        while(left >=0 and right < length and s[left] == s[right]):
            left -= 1
            right += 1
        
        return right - left - 1
 

ips='ababbbabac'
substring = longestPalindrome(inps)
