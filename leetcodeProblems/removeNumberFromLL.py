class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = None
          
          
class Solution:

    def printList(self, removelist):
        while(removelist):
            print(removelist.val)
            removelist = removelist.next
            
            
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #if the list is empty return nothing
        if(head is None):
            return
        
        prev = ListNode(head.val)
        temp = prev
        
        while(head):
            if head.val == val:
                pass
            else:
                temp.next = ListNode(head.val)
                temp = temp.next #update the pointer
            
            head = head.next #update to the next pointer
        
        return self.printList(prev.next)
        
        
ll = [1,2,3,6,4,5,6,7]
print(Solution().removeElements(ll, 6))
