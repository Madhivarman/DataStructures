"""
    Problem Statement:
        Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
        in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives
        the sum of target.
"""
def fourSum(asList, target):
        res = set()
        asList = sorted(asList)
        ln = len(asList)

        for left in range(ln - 3):
            right = ln - 1

            #special condition
            while left < right - 2:
                a = asList[left]
                d = asList[right]
                #inner pointers
                left_inner = left + 1
                right_inner = right - 1

                #iterate through the loops
                while left_inner < right_inner:
                    b = asList[left_inner]
                    c = asList[right_inner]
                    isSum = a + b + c + d

                    if isSum < target:
                        left_inner += 1
                    elif isSum > target:
                        right_inner -= 1
                    else:
                        res.add((a, b, c, d))
                        right_inner -= 1
                        left_inner += 1
                
                #decrease the right pointer by 1
                right -= 1


        return list(res)


case1 = [1, 0, -1, 0, -2, 2]
case2 = [-10, 2, 1, 0, 4, -4, 10]
case3 = [0,0,0,0]
case4 = [-4,0,-4,2,2,2,-2,-2]
case5 = [-3,-1,0,2,4,5]

target = 0
target2 = 4
target4 = 7
target5 = 0

ss = fourSum(case2, target2)
print(ss)