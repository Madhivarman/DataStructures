"""
    Problem Statement:
        In a row of trees, the i-th tree produces fruit with type tree[i].
        You start at any tree of your choice, then repeatedly perform the following steps:
        
        Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
        Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
        Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

        You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
        
        What is the total amount of fruit you can collect with this procedure?
"""
class Solution():
    def totalFruitWeCanTake(self, trees):
        index = 0
        fruit_map = {} #hashmap
        fruit_count = 0
        fruit_type = 0
        total_fruits = 0

        for i in range(len(trees)):
            if trees[i] not in fruit_map:
                fruit_map[trees[i]] = 1
                fruit_type += 1

                if fruit_type >  2:
                    total_fruits = max(total_fruits, fruit_count)

                    while(len(fruit_map) > 2):
                        #print(fruit_map, total_fruits)
                        if fruit_map[trees[index]] > 1:
                            fruit_map[trees[index]] -= 1 #decrement
                        elif fruit_map[trees[index]] == 1:
                            del fruit_map[trees[index]]

                        index += 1 #increment the index
                        fruit_count -= 1 #decrement the fruit count
                    
                    fruit_type -= 1 #decrement the fruit type
                
                fruit_count += 1 #increment the count

            else:
                fruit_map[trees[i]] += 1
                fruit_count += 1
        
        total_fruits = max(total_fruits, fruit_count)
    
        return total_fruits



tc1 = [1,2,1]
tc2 = [0,1,2,2]
tc3 = [1,2,3,2,2]
tc4 = [3,3,3,1,2,1,1,2,3,3,4]

print(Solution().totalFruitWeCanTake(tc1))
print()
print(Solution().totalFruitWeCanTake(tc2))
print()
print(Solution().totalFruitWeCanTake(tc3))
print()
print(Solution().totalFruitWeCanTake(tc4))
print()