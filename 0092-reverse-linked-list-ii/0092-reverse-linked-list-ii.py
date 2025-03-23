# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        # if node index is given use below code to find the nodes
        index = 1
        node = head
        prev_node = left_node = right_node = None
        
        while node!=None:
            if index == left-1:
                prev_node = node
            if index == left:
                left_node = node
            if index == right:
                right_node = node
            node=node.next
            index +=1
        
        # if node value is given use below code to find the nodes
        """
        left_node = right_node = None

        # getting the right node
        node = head
        while node and node.val!=right:
            node = node.next
        right_node = node

        # getting the left node and node previous to left
        prev_node = None
        node = head
        while node and node.val!=left:
            prev_node = node
            node = node.next
        left_node = node
        """
        if left_node is None or right_node is None:
            return head 

        # node previous than left should point to the right node directly
        if prev_node is None:
            head = right_node
        else:
            prev_node.next = right_node
        curr_node = left_node
        # curr_node.next = right_node.next

        while prev_node!=right_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp

        left_node.next = curr_node
        return head