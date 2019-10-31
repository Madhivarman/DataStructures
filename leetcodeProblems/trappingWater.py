class Solution():

    def logic(self, ce, ms, output):
        if ce >= ms:
            ms = ce
        else:
            output += ms - ce
        
        return output, ms

    def trapWater(self, height):
        output = 0
        if height is None:
            pass
        else:
            #get the index for the heightest bar
            maxIndex = height.index(max(height))
            maxSeen = 0

            #iterate from left to that index
            for i in range(maxIndex):
                output, maxSeen = self.logic(height[i], maxSeen, output)
                """if height[i] >= maxSeen:
                    maxSeen = height[i]
                else:
                    output += maxSeen - height[i]"""
            
            #now iterate through right
            maxSeen = 0
            #traverse reverse
            for i in range(len(height)-1, maxIndex-1, -1):
                output, maxSeen = self.logic(height[i], maxSeen, output)

        return output


tc1 = [0,1,0,2,1,0,1,3,2,1,2,1] #6
tc2 = [4,2,3] #1
tc3 = [1,7,5,2] #0

capacityWeCanHold = Solution().trapWater(tc3)
print("Capacity We can Hold:{}".format(capacityWeCanHold))