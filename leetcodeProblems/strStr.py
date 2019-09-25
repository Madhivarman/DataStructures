"""
    Problem Statement:
        Return the index of the first occurrence of needle in haystack, 
        or -1 if needle is not part of haystack.
"""
def strStr(haystack, needle):
    needle_pointer = 0
    index = 0
    startindex = 0
    re = []
    bool = False
    if needle in haystack:
        bool = True
    
    if bool:
        for i in range(0, (len(haystack) - len(needle)) + 1):
            substring = haystack[i:i+len(needle)]
            print(substring)
            if substring == needle:
                return i 
    else:
        return -1


s = strStr("mississipi", "issip")
s2 = strStr("aaaa", "aab")
print(s2)