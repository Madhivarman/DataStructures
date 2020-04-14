"""
    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left justified and no extra space is inserted between words.

    Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
"""
from collections import deque
import math

class Solution():
    def fulljustification(self, low, maxWidth):
        result = [] #to store the result
        queue = deque() #to store the words

        line = maxWidth
        a = 0

        #iterate through each words
        for word in low:
            #to check if queue has reached the maximum width
            if len(queue) + a + len(word) <= maxWidth:
                queue.append(word)
                #update the params
                line -= len(word)
                a += len(word)
            else:
                current_state = '' #to add string

                #iterate through the queue
                while queue:
                    ##calculate the spacing
                    spacing = None
                    if len(queue) == 1:
                        spacing = line
                    else:
                        spacing = int(math.ceil(line/(len(queue) - 1.0)))


                    current_state += queue.popleft()
                    if line - spacing > 0:
                        current_state += ' ' * spacing
                    elif line > 0:
                        current_state += ' ' * line
                    
                    line -= spacing #update the line
                
                #append to the result
                result.append(current_state)
                #append the current word to the queue
                queue.append(word)
                line = (maxWidth - len(word))
                a = len(word)
        
        t = ''
        while queue:
            t += queue.popleft()
            if line:
                t += " "
                line -= 1
        
        if line:
            t += (' '*line)
        
        result.append(t)
        return result


tc1 = ["This", "is", "an", "example", "of", "text", "justification."]
tc1_maxwidth = 16

tc2 = ["What","must","be","acknowledgment","shall","be"]
tc2_maxwidth = 16

tc3 = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
tc3_maxwidth = 20


print(Solution().fulljustification(tc1, tc1_maxwidth))
print(Solution().fulljustification(tc2, tc2_maxwidth))
print(Solution().fulljustification(tc3, tc3_maxwidth))