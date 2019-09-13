"""
    Given a string, the output should write in
    zig-zag pattern.
"""
def zigzagPattern(s, numrows):
    #if length of string is 1, return the original string
    if numrows == 1:
        return s
    if len(s) == 0:
        return 

    N = len(s) #getting the length of the string

    #get the minimum number of row
    rows = ['']*min(len(s), numrows)

    #normally the step pointer will be 0
    #it should iterate till numrows.
    #if it reaches the lastrow, it should come reverse
    #and if it reaches again it should move forward

    start = 0 
    isgoingDown = False
    
    for i in range(len(s)):
        print(start)
        rows[start] += s[i] #get the current row and append
        
        #condition
        if start == 0  or start == numrows - 1:
            isgoingDown = not(isgoingDown)
        
        #if still its going down then increment it
        #else decrement
        if isgoingDown:
            start += 1
        else:
            start -= 1
    

    pattern = "".join(rows)
    return pattern


response = zigzagPattern("Madhivarman", 4)
print(response)

