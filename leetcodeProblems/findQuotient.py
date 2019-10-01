"""
    Problem statement:
        Given two integers dividend and divisor, divide two integers without using multiplication,
        division and mod operator.
        Return the quotient after dividing dividend by divisor.
        The integer division should truncate toward zero.
"""
def divide(self, dividend: int, divisor: int) -> int:
        overflow = 2147483647
        quotient=0
        
        if dividend == -2147483648 and divisor == -1:
            return overflow
        
        if divisor == 1:
            return dividend
        
        isnegative = (dividend < 0) ^ (divisor < 0) #returns True or False
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        #find how many perfect bit operations are there
        #subtract with dividend and find how many perfect
        #bit operations are there. Carry this loop
        while dvd >= dvs:
            tmp = dvs
            m = 1
            
            #iterate through the last perfect bit operator
            while tmp << 1 <= dvd:
                tmp <<= 1
                m <<= 1
            
            dvd -= tmp #update the value
            quotient += m #update the quotient value
        
        if not isnegative:
            return quotient
        else:
            return ~quotient + 1 #return the value as negative


q = divide(24, 5)
print(q)