"""
     finding the median of two arrays with O(log(m+n)).
     Gist:
        a: [a1,a2,a3,a4,a5], b:[b1, b2,b3,b4, b5]
        find the partition point for both the array. 
        consider that the partitioning is happened at a :[[a1,a2],[a3,a4,a5]],
        b:[[b1, b2], [b3,b4,b5]]
        and if this is the test case if a2 <= b3 and b2 <= a3 then if the length of the 
        partioned array is odd then avg(max(a2, b2), min(a3, b3)) if the length
        is even then max(a2, b2)
"""
import math

def findMedianFromTwoList(l1, l2):

	 	median = 0
        #check the length of both lists
        length_l1, length_l2 = len(nums1), len(nums2)

        if length_l1 > length_l2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = length_l1

        while(low <= high):

            partition_x = math.floor((low+high) / 2)
            partition_y = math.floor((length_l1 + length_l2 + 1) / 2) - partition_x

            #pointer
            if partition_x == 0:
                maxLeftX = float("-inf")
            else:
                maxLeftX = nums1[partition_x - 1]


            if partition_x == length_l1:
                minRightX = float("inf")
            else:
                minRightX = nums1[partition_x]


            #for list 2 data

            if partition_y == 0:
                maxLeftY = float("-inf")
            else:
                maxLeftY = nums2[partition_y-1]

            if partition_y == length_l2:
                minRightY = float("inf")
            else:
                minRightY = nums2[partition_y]

            #main logic and condition
            if (maxLeftX <= minRightY) and (minRightX >= maxLeftY):
                #if it obeys the logic check whether its odd or even
                if ((length_l1 + length_l2) %2 == 0):
                    #if its even
                    median = float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                    return median
                else:
                    median = float(max(maxLeftX, maxLeftY))
                    return median

            elif maxLeftX > minRightY:
                high = partition_x - 1
            else:
                low = partition_x + 1


        return median


l1 = [1,2,3,5,6]
l2 = [4]

median = findMedianFromTwoList(l1, l2)
print(median)