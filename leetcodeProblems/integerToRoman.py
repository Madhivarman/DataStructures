"""
    Problem Statement:
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
        {I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
"""

def convertNumericToInteger(asDictionary, numberToConvert):
    string = ''
    keysAsReverse = reversed(sorted(asDictionary.keys()))

    for key in keysAsReverse:
        while(numberToConvert >= key):
            string += asDictionary[key]
            numberToConvert -= key
    
    return string




mapping = { 1 : 'I',4 : 'IV',5 : 'V', 9 : 'IX',10 : 'X', 40 : 'XL',50 : 'L',90 : 'XC',100 : 'C',400 : 'CD',500 : 'D',900 : 'CM',1000 : 'M'}
convertedRoman = convertNumericToInteger(mapping, 45)
print(convertedRoman)