# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        
        # curr_val = head.val
        node = head
        while node.next!=None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        
        return head
        

