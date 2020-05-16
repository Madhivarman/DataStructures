"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and 
it is guaranteed an answer exists.
"""
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        n = len(barcodes)
        result = [0] * n
        #less than 2, just return the list
        if n <= 2:
            return barcodes
        
        hashmap = Counter(barcodes)
        sorted_array = []

        for key, value in hashmap.most_common():
            sorted_array.extend([key] * value)
        
        pointer = 0

        for i in range(0, n, 2):
            result[i] = sorted_array[pointer]
            pointer += 1 #increment the pointer
        
        for i in range(1, n ,2):
            result[i] = sorted_array[pointer]
            pointer += 1
        

        return result
