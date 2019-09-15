"""
    Problem Statement:
        Write a function to find the longest common prefix string amongst an array of strings.
"""
def findingLongestPrefix(asList):
    longestprefix = ""

    #get number of elements in the list
    listLength = len(asList)
    minimumChar = len(asList[0]) #set to the highest as initial
    dump = [] #storing as dump
    dump.append(asList[0])
    
    for i in range(1, listLength):
        #get the current string
        currentString = asList[i]
        #get the minimum length
        minimumLength = min(len(dump[0]), len(currentString))
        j = 0

        while(j < minimumLength):
            if currentString[j] == dump[0][j]:
                    longestprefix += currentString[j]
            else:
                break 
            
            
            #increment j
            j += 1
        
        #pop the first element and append the current element
        dump.pop(0)
        dump.append(currentString)
        
        #check the minimum character
        if j <= minimumChar:
            minimumChar = j

        #update the currentstring with length
        longestprefix = longestprefix[:minimumChar]
    
    if len(longestprefix) == 0:
        return " "
    else:
        return longestprefix
    
def easySolution(asList):
    if asList is None or len(asList) == 0:
            return ""
        else:
            prefix = asList[0]
            for i in range(1, len(asList)):
                while asList[i].find(prefix) != 0:
                    prefix = prefix[:len(prefix)-1]
                    if len(prefix) == 0:
                        return ''
        
        return prefix


arrays = ["aa","aab","aabbc"]
prefix = findingLongestPrefix(arrays)
print(prefix)