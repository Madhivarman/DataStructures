"""
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees 
    of every node never differ by more than 1.
"""
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():

    def InorderTraversal(self, root, stack):
        if root:
            self.InorderTraversal(root.left, stack)
            stack.append(root.val)
            self.InorderTraversal(root.right, stack)
        
        return stack

    def formTree(self, lists):
        if not(lists):
            return
        n = len(lists) #length of the lists
        main_node = n // 2
        root = TreeNode(lists[main_node])

        #left
        root.left = self.formTree(lists[:main_node])
        #right
        root.right = self.formTree(lists[main_node+1:])

        return self.InorderTraversal(root, [])

    def sortListToBST(self, root):
        stack = []
        #iterate through the linked list
        while(root):
            stack.append(root.val)
            root = root.next #update the pointer

        return self.formTree(stack)


n1 = ListNode(-10)
n2 = ListNode(-3)
n3 = ListNode(0)
n4 = ListNode(9)
n5 = ListNode(5)

root = n1
root.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(Solution().sortListToBST(root))

