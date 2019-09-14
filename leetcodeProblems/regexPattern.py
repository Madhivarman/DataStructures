"""
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    Note:
        Entire pattern of the string should match. If we do lenth equal in this case, it won't pass
        all the test cases.
        For example:
            s = aab
            p = *b should return True
"""

def regexExpression(string, pattern):
    #using dynamic programming technique
    #set up the matrix
    row = len(string) + 1
    column = len(pattern) + 1
    #initially all fill up with zero
    matrix = [[0 for col in range(column)] for y in range(row)]

    matrix[0][0] = 1 #i=0, j=0 value=1

    for colpointer in range(1, column):
        if pattern[colpointer-1] == '*':
            matrix[0][colpointer] = matrix[0][colpointer-2]
    
    """
        3-Conditions

        1. if the current pointers in string and pattern are same assign previous 
        pointer element.

        2. If '*' in pattern go to 2 element back in pattern. If the previous element
        in string and 2 elements before in pattern do the Exclusive OR operation to the current
        and previous element.
        
        3. If the current pointers in string and pattern are not same, assing zero
    """
    
    #string iteration
    for rowpointer in range(1, len(matrix)):
        #pattern iteration
        for colpointer in range(1, len(matrix[0])):
            #1 condition
            if (string[rowpointer-1] == pattern[colpointer-1]) or (pattern[colpointer-1] == '.'):
                matrix[rowpointer][colpointer] = matrix[rowpointer-1][colpointer-1]
            
            #2 condition
            elif (pattern[colpointer-1] == '*'):
                matrix[rowpointer][colpointer] = matrix[rowpointer][colpointer-2]
                if (string[rowpointer-1] == pattern[colpointer-2]) or (pattern[colpointer-2] == '.'):
                    #seeing the value at top operat
                    matrix[rowpointer][colpointer] |= matrix[rowpointer-1][colpointer]
            
            else:
                matrix[rowpointer][colpointer] = 0 #false
    

    if matrix[row-1][column-1]:
        return True
    else:
        return False


ismatched = regexExpression("xaabyc","xaab.c")

print("Is string Matched:{}".format(ismatched))