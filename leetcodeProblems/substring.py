#function to find the longest substring length
def solution_one(string):
    chars = 256
    visited = [-1] * chars
    curr_len = 1 #initial settings
    max_len = 1  #initial settings
    length = len(string) #length
    previous_index = 0
    
    #make first string as visited
    visited[ord(string[0])] = 0

    for i in range(1, length):
        #check if current character is not marked as visited
        previous_index = visited[ord(string[i])]

        #check if current character is not present in NRSC
        #then do curr_len increment

        if previous_index == -1 or (i - curr_len > previous_index):
            curr_len += 1 #increment it

        #if the current character is already present in the substring
        #then update NRCS to start from next character.
        else:
            #when we are considering this change then we need to check
            #if current length is greater than maximum length of not
            if curr_len > max_len:
                max_len = curr_len  #make changes
            
            curr_len = i - previous_index
        
        #update the index of current character
        visited[ord(string[i])] = i
    

    #check if last current length is greater than max length
    if curr_len > max_len:
        max_len = curr_len

    return max_len


def solution_two(s):
    dict_value = {}
    start=0 
    maxi = 0

    for i, value in enumerate(s):
        if value in dict_value:
            sums = dict_value[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxi:
            maxi = num
        dict_value[value] = i
    
    return maxi

usecase1 = "abcabcbb" #3
usecase2 = "bbbbb" #1
usecase3 = "pwwkew" #3
usecase4 = "geeksforgeeks" #7
usecase5 = "b00adfadsf" #4
usecase6 = "au" #2
usecase7 = "dvdf" #3
usecase8 = "ABDEFGABEF" #6
usecase9 = "anviaj" #5
usecase10 = "madhivarman" #7


aslist = [usecase1, usecase2, usecase3, usecase4, usecase5, usecase6, usecase7, usecase8, usecase9, usecase10]

for l in aslist:

    length = solution_two(l)
    print("longest Substring Length:{}".format(length))

    print("-" * 15)
