"""
    Problem Statement:
        An image is represented by a 2-D array of integers, each integer representing the pixel value
        of the image (from 0 to 65535).

        Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a 
        pixel value newColor, "flood fill" the image.

        To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
        to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
        to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the 
        aforementioned pixels with the newColor.

        At the end, return the modified image.
"""

from collections import deque

class Solution():
    def floodfill(self, image, sr, sc, newColor):
        #row and columns
        row, cols = len(image), len(image[0])
        q = deque([])
        q.append([sr, sc]) #start from the row and column
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while(q):
            #current row, current col
            cr, cc = q.popleft()
            color, image[cr][cc] = image[cr][cc], newColor

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                
                if 0 <= nr < row and 0 <= nc < cols and color == image[nr][nc] != newColor:
                    q.append([nr, nc]) #append to the queue

        return image

tc1 = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2

print(Solution().floodfill(tc1, sr, sc, newColor))
