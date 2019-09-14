"""
    Problem Statement:
        converting Roman Integers to String
"""
def RomanToInteger(string):
    asMap = {'IX': 9, 'C': 100, 'CM': 900, 'XL': 40, 'I': 1, 'XC': 90,
    'M': 1000, 'L': 50, 'CD': 400, 'V': 5, 'X': 10, 'IV': 4, 'D': 500}

    if string in asMap.keys():
        return asMap[string]
    
    integer = 0

    while(string !=''):
        try:
            integer += asMap[string[:2]]
            string = string[2:]
        except:
            integer += asMap[string[0]]
            string = string[1:]


    return integer


rtoI = RomanToInteger("MCMXCIV")
print(rtoI)