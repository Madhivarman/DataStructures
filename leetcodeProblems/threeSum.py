"""
    Problem Statement:
        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
        Find all unique triplets in the array which gives the sum of zero.
"""

def findThreeIntegers(asList):
    solutionSet = []
    #handling null cases
    if len(asList) == 0:
        return solutionSet

    #sort the arrays
    asList = sorted(asList)
    
    for i in range(len(asList)):

        left = i+1
        right = len(asList) - 1

        while(left < right):
            isZero = asList[i] + asList[left] + asList[right]

            if isZero == 0:
                temp = [asList[i], asList[left], asList[right]]
                solutionSet.append(temp)

                leftValue = asList[left]

                while(left < len(asList) and asList[left] == leftValue):
                    left += 1
                
                rightValue = asList[right]
                while(right > left and asList[right] == rightValue):
                    right -= 1
            
            elif isZero < 0:
                left += 1
            
            else:
                right -= 1
    
    #remove duplicates
    solutionSet = [list(tupl) for tupl in {tuple(item) for item in solutionSet }]
    return solutionSet


ss = findThreeIntegers([-1, 0, 1, 2, -1, -4])
print(ss)