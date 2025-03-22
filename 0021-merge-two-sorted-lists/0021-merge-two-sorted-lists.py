# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        l1 = list1
        l2 = list2

        if l1.val<l2.val:
            new_list_node = ListNode(list1.val)
            l1 = l1.next
        else:
            new_list_node = ListNode(list2.val)
            l2 = l2.next
        
        new_list_head = new_list_node
        
        while l1 and l2:
            if l1.val < l2.val:
                new_list_node.next = ListNode(l1.val)
                new_list_node = new_list_node.next
                l1 = l1.next
                
            else:
                new_list_node.next = ListNode(l2.val)
                new_list_node = new_list_node.next
                l2 = l2.next
                
        while l1:
            new_list_node.next = ListNode(l1.val)
            new_list_node = new_list_node.next
            l1 = l1.next
        
        while l2:
            new_list_node.next = ListNode(l2.val)
            new_list_node = new_list_node.next
            l2 = l2.next
            
        return new_list_head 