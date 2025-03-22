# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        cycle_index = -1
        cycle_node = None
        while fast!=None and fast.next!=None:

            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                cycle_index = 0
                cycle_node = head
                while cycle_node!=slow:
                    cycle_node=cycle_node.next
                    slow = slow.next
                    cycle_index+=1
                break
        return cycle_node