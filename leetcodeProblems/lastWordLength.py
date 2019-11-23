def lengthOfLastWord(string_):
    string_split = string_.split()
    if len(string_split) == 0:
        return 0
    else:
        return len(string_split[-1])

r = lengthOfLastWord('a ')
print(r)