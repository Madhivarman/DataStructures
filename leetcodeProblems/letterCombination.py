def letterCombinations(digits, dictionary):
    combinations = []
    currentCombination = ['']

    if len(digits) == 0 or digits not in '23456789':
        return []
    
    def combine(cb, d):
        letL = []
        for pre in cb:
            for char in dictionary[d]:
                letL.append(pre+char)
        
        return letL
    
    for digit in digits:
        currentCombination= combine(currentCombination, digit)
    
    return currentCombination


dialpad = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
 } #number and its key

returnedList = letterCombinations('234', dialpad)
print(returnedList)