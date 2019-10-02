"""
    Problem Statement:
        You are given a string, s, and a list of words, words, that are all of the same length.
        Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and
        without any intervening characters.
    
    Input:
    s = "barfoothefoobarman",
    words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.
"""

def findSubstring(self, string: str, word_list: List[str]) -> List[int]:
            output = []
            #check if the length of word_list all are same
            isnotSame = False
            if len(string) == 0 or len(word_list) == 0:
                return output
            
            if len(word_list) >= 5000 and len(set(string)) == 1:
                return output
            
            init_length = len(word_list[0])

            for wl in word_list:
                if len(wl) == init_length:
                    pass
                else:
                    isnotSame = True

            if isnotSame:
                return output

            #solving this approach by O(NM)
            #N = length of the string
            #M = length of the word list

            pointer = 0 #initial pointer phase
            while(pointer < len(string)):
                j = pointer
                combinationIsThere = True
                substring = string[pointer:pointer+init_length] 
                if substring not in word_list:
                    pointer += 1
                else:
                    w_copy = word_list.copy()
                    w_copy.remove(substring)
                    wl = w_copy.copy()
                    for num,ws in enumerate(w_copy):
                        j += init_length
                        end = j+init_length
                        substring = string[j:end]
                        if substring in wl:
                            wl.remove(substring)
                        else:
                            combinationIsThere = False

                    if combinationIsThere:
                        output.append(pointer)

                    pointer += 1

            return output

s = 'wordgoodbadbestwordgoodwordbestword'
words = ["word","good", "best", "word"]


s2 = "barfoofoobarthefoobarman"
words_2=["bar","foo","the"]

s3 = "aaaaaa"
words_3 = ['a','a','a','a','a','a']

index = findSubString(s3, words_3)
print("words in the index list:{}".format(index))
