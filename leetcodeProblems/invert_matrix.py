class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        r = len(A)
        result = []
        for i in range(r):
            col = A[i]
            col[:] = col[::-1]
            temp = []
            for bit in col:
                if bit:
                    temp.append(0)
                else:
                    temp.append(1)
            result.append(temp)
        return result
