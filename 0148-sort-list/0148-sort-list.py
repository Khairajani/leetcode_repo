# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        prev = head

        while fast!=None and fast.next!=None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        return slow

        print("merging",head.val, mid.val, tail.val)
        list1 = head
        list2 = mid.next

        if list1 is None and list2 is None:
            print("fuck up")
            head = None
            return head
            # return None
        
        if list1 is None:
            print("fuck up")
            head = list2
            return head
            # return list2
        
        if list2 is None:
            print("fuck up")
            head = list1
            return head
            # return list1

        l1 = list1
        l2 = list2

        if l1.val<l2.val:
            new_list_node = ListNode(list1.val)
            l1 = l1.next
        else:
            new_list_node = ListNode(list2.val)
            l2 = l2.next
        
        new_list_head = new_list_node
        
        while l1 and l1!=mid.next and l2 and l2!=tail:
            if l1.val < l2.val:
                new_list_node.next = ListNode(l1.val)
                new_list_node = new_list_node.next
                l1 = l1.next
                
            else:
                new_list_node.next = ListNode(l2.val)
                new_list_node = new_list_node.next
                l2 = l2.next
                
        while l1 and l1!=mid.next:
            new_list_node.next = ListNode(l1.val)
            new_list_node = new_list_node.next
            l1 = l1.next
        
        while l2 and l2!=tail:
            new_list_node.next = ListNode(l2.val)
            new_list_node = new_list_node.next
            l2 = l2.next
        
        head = new_list_head
        while (new_list_head):
            print("x",new_list_head.val, end=" -> ")
            new_list_head = new_list_head.next
        print("")
        # print("hehe",new_list_head.val)
        # return new_list_head 

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
        
        xnode = new_list_head
        while xnode:
            print(xnode.val,end="->")
            xnode = xnode.next
        print()
        return new_list_head

    def mergeSortLL(self, head) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid = self.middleNode(head)
        print(head.val, mid.val)
        head = self.mergeSortLL(head)
        mid = self.mergeSortLL(mid)
        return self.mergeTwoLists(head,mid)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # tail = head
        # while tail.next is not None:
        #     tail = tail.next
        return self.mergeSortLL(head)