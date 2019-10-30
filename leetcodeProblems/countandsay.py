def countAndSay(n):
        if n <= 1:
            return "1"
        prevCountAndSay = countAndSay(n - 1)
        last = None
        occurrence = None
        output = ""
        for i in prevCountAndSay:
            if last is not None:
                if i == last:
                    occurrence += 1
                else:
                    output += str(occurrence) + last
                    occurrence = 1
            else:
                occurrence = 1
            last = i
        return output if occurrence is None else output + str(occurrence) + last
    
  
result = countAndSay(5) #prints 111221
