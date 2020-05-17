"""
You are given a doubly linked list which in addition to the next and previous pointers, 
it could have a child pointer, which may or may not point to a separate doubly linked list. These child
lists may have one or more children of their own, and so on, to produce a multilevel data structure, 
as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given 
the head of the first level of the list.
"""

class Node():
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution():

    #Utility Function
    def flattenDoubleLinkedListUtil(self, head, result):

        if head is None:
            return None
        else:
            print("entered:{}".format(head.val))
            result.append(head.val)
        
        child = self.flattenDoubleLinkedListUtil(head.child, result)    
        next_ = self.flattenDoubleLinkedListUtil(head.next, result)

        return result
    

    def flattenDoubleLinkedListAsList(self, head, stack):
        #if empty
        if head is None:
            return head

        node = head

        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)

                temp = node.child
                node.next = temp
                temp.prev = None
                node.child = None
            
            elif not node.child and stack:
                temp = stack.pop()
                node.next = temp
                temp.prev = node

            node = node.next #update the node
        
        return head
    

    def flattenDoubleLinkedList(self, head):
        result = []
        #return the response just as list
        res = self.flattenDoubleLinkedListUtil(head, result)

        #return response as double linked list
        res2 = self.flattenDoubleLinkedListAsList(head, stack=[])


#individual nodes
head = Node(1, None, Node(2, None, None, None), Node(3, None, None, None))

print("Next Ele:{}".format(head.next))
print("Child:{}".format(head.child))

print(Solution().flattenDoubleLinkedList(head))