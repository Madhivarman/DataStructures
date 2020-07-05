class Solution():
    def hammingDistance(self, x, y):
        if x == y:
            return 0
        
        #using XOR operator
        z = x ^ y
        z = bin(z)
        
        return z.count('1')
    
    def withoutOperator(self, x, y):
        xb = bin(x)
        yb = bin(y)
        
        xb = xb[2:]
        yb = yb[2:]
        
        #calculate the difference and fill with zero's      
        if len(xb) > len(yb):
            diff = len(xb) - len(yb)
            yb = '0'*diff + yb
        
        if len(xb) < len(yb):
            diff = len(yb) - len(xb)
            xb = '0'*diff + xb
        
        print(xb, yb)
        
        count = 0
        
        for i in range(len(xb)):
            if xb[i] != yb[i]:
                count += 1
        
        return count
   
