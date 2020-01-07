"""
    Problem Statement:
        Find the value closest to Zero
"""
#return value that is near to zero
def closestToZero(aslist):
    sofarClose = aslist[0] #assign the first index
    for val in aslist[1:]:
        if val < 0:
            if sofarClose > val:
                if sofarClose > 0 and abs(val) < sofarClose:
                    sofarClose = val
            else:
                sofarClose = val
        else:
            if abs(sofarClose) >= val:
                sofarClose = val
    return sofarClose

tc1 = [7,-10, 13, 8, 4, -7, -12, -3, 3, -9, 6, -1, -6, 7]
tc2 = [-4, -7, -13, 1, 8, 12, 6, -5]
tc3 = [1, -2, -8, 4, 5]
tc4 = [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]


print(closestToZero(tc4))
