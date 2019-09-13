"""
    1.should remove only one white space until the required character is found.
    2.if the words comes after the numerical records,should be ignored.
    3.if the words comes as prefix of numericals should return 0
    4.if the return value is lies within a range [-2^31, 2*31-1] then
    it representables values Integer.Min and Integer.Max should return.
    5.Special characters should not come at first
"""
def atoi(str):
    str = str.lstrip()
    if(len(str)==0):
        p = 0
    elif(str[0]=="-" or str[0]=="+"):
            i = 1
            if(len(str)>1):
                while(i<len(str) and str[i] in "0123456789"):
                    i+=1
                if(i>1):
                    p = (int(str[0:i]))
                else:
                    p = 0
            else:
                p = 0
    elif(str[0] in "0123456789"):
            i = 1
            if(len(str)>1):
                while(i<len(str) and str[i] in "0123456789"):
                    i+=1
                p = int(str[0:i])
            else:
                p = (int(str))
    else:
            p = 0
    
    z = 2**31
    if(p>=z):
        p = z-1
    elif(p<-z):
        p = -z
    
    
    return p

stringToInteger = atoi("892")
print(stringToInteger)