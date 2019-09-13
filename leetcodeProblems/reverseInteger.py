def reverseInteger(n):
    #divide by 10 and store the remainder
     if n > 0:
            a = int(str(n)[::-1])
        
        if n <= 0:
            a = -1 * int(str(n*-1)[::-1])
        
        #bit overflow
        mini = -2**31
        maxi = 2**31 - 1
        
        if a not in range(mini, maxi):
            return 0
        
        return a


rint = reverseInteger(-2147483648)
print(rint)

    