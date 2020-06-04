"""
    Problem Statement:
        You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
        What is the maximum number of envelopes can you Russian doll? (put one inside other)
        Note:
        Rotation is not allowed.
"""
class Solution():
    def totalEnvelopeFits(self, cards):
        output = 0
        #sort the cards by width
        cards.sort(key = lambda x: x[0])
        
        max_envelops = []

        for i, env in enumerate(cards):
            stack_length = 1 #number of envelops we can stack  so far
            for j in range(0, i):
                #condition
                if env[0] > cards[j][0] and env[1] > cards[j][1]:
                    current_length = max_envelops[j] + 1 #get current length
                    #assign maximum
                    if current_length > stack_length:
                        stack_length = current_length

            max_envelops.append(stack_length)

            #to return maximum
            if stack_length >  output:
                output = stack_length

        return output


tc1 = [[5,4],[6,4],[6,7],[2,3]]
tc2 = [[5,4],[6,4],[6,7],[2,3],[1,2],[7,8],[9,10]]

print(Solution().totalEnvelopeFits(tc1))
print(Solution().totalEnvelopeFits(tc2))
