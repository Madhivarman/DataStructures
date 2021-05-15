class Solution:
    def isNumber(self, s: str) -> bool:
        #create accepted characters
        accepted_chars = "0123456789+-eE."
        numbers = '1234567890'
        stack = [] #stack to store the characters
        
        #base conditions
        if s.count('.') > 1 or s.count('e') > 1 or s.count('E') > 1:
            return False
        
        if len(s) == 1 and s in ('+','-', '.', 'e', 'E'):
            return False
        
        #check if there are no numbers
        aslists = [x for x in s]
        if Solution.check_digit_present(aslists,numbers) == False:
            return False
        
        for i in range(len(s)):
            curr = s[i]
            #base condition
            if curr not in accepted_chars:
                # print("condition failed on, because of invalid char: {}".format(curr))
                return False
            
            #append to the stack, if simply its digit
            if Solution.isdigit(curr):
                stack.append(curr)
            
            #sign conditions
            if curr == '-' or curr == '+':
                if len(stack) == 0 or stack[-1] in ('e', 'E'):
                    stack.append(curr)
                else:
                    # print("condition failed while checking (-+)")
                    return False
            
            #dot conditions
            if curr == '.':
                if len(stack) == 0 or stack[-1] in ('+','-'):
                    pass
                if "e" in stack or "E" in stack:
                    # print("condition failed while checking (.)")
                    return False
                stack.append(curr)
            
            #e or E condition
            if curr == 'e' or curr == 'E':
                if len(stack) == 0 or stack[-1] in ('+','-',):
                    #print("condition failed while checking (e/E)")
                    return False
                #if no numbers are there before E, return False
                if Solution.check_digit_present(stack, numbers) == False:
                    return False
                stack.append(curr)
        
        #last character check, because these sign should be
        #followed by digits
        if stack[-1] in ('+', '-', 'e', 'E'):
            # print(stack)
            # print("condition failed on last Checkpoint")
            return False
        return True
            
    
    @staticmethod
    def isdigit(character):
        try:
            asint = int(character)
            return True
        except Exception:
            return False
    
    @staticmethod
    def check_digit_present(stack, numbers):
        flag = False
        for char in numbers:
            if char in stack:
                flag = True
                break
        return flag
