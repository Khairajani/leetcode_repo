# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIterative(self, head):
        # if empty or only-one element in linked list return head directly
        if head == None or head.next == None:
            return head

        # else reverse the elements of linked list
        prev = head
        curr = head.next

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = None
        head = prev
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListIterative(head)
        