"""
    Problem Statement:
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
"""
def isValid(string):
    stack = []
    pairs  = {
        '{':'}',
        '(':')',
        '[':']',
        '}':'{',
        ')':'(',
        ']':'['
    }

    for i in string:
        print("current element:{}, stack:{}".format(i, stack))
        if len(stack) == 0:
            stack.append(i)
        else:
            currentlast = stack[-1]
            if pairs[i] == currentlast or pairs[currentlast] == i:
                stack = stack[:-1]
            else:
                stack.append(i)
    

    if len(stack) == 0:
        return True
    else:
        return False


boolean = isValid("[([]])")
print(boolean)