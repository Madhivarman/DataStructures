"""
    Problem Statement:
        Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""
class Solution():

    def findLargestRectange(self, histogram):
        keep_track = []
        maximum_area = 0
        index = 0

        while(index < len(histogram)):
            if len(keep_track) == 0 or histogram[keep_track[-1]] <= histogram[index]:
                keep_track.append(index)
                index += 1
            else:
                top_of_stack = keep_track.pop()
                if len(keep_track) == 0:
                    area = histogram[top_of_stack] * index
                else:
                    area = histogram[top_of_stack] * (index - keep_track[-1] - 1)
                
                maximum_area = max(area, maximum_area)
        
        while(keep_track):
            top_of_stack = keep_track.pop()
            if len(keep_track) == 0:
                area = histogram[top_of_stack] * index
            else:
                area = histogram[top_of_stack] * (index - keep_track[-1] - 1)
            
            maximum_area = max(maximum_area, area)
        
        return maximum_area

    def maximumRectange(self, grid):
        stack = [0 for _ in range(len(grid[0]))]
        maxi_area = 0

        for rows in range(len(grid)):
            for num, i in enumerate(grid[rows]):
                if i == '0':
                    stack[num] = 0
                else:
                    stack[num] += 1
            
            #find the largest Rectange
            maximumareasofar = self.findLargestRectange(stack)
            maxi_area = max(maxi_area, maximumareasofar)

        return maxi_area


tc1 = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(Solution().maximumRectange(tc1))