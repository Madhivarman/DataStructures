class Solution:
    def reverseBits(self, n: int) -> int:
        asbin = bin(n)

        if len(asbin) == 32:
            asbin = "0"*2 + str(asbin[2:])
        else:
            temp = asbin[2:]
            diff = 32 - len(temp)
            asbin = "0"*diff + str(temp)
        
        reverse_string = []
        pointer = len(asbin) - 1
        
        while(pointer >= 0):
            reverse_string.append(asbin[pointer])
            pointer -= 1
        
        result = int("".join(reverse_string), 2)
        
        return result