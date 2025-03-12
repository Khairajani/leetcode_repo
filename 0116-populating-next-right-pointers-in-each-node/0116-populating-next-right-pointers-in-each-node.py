"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        if not root:
            return root
        # Approach 1: with plain LOT or BFS using queue and level_list
        """ 
        queue_ds = [root]
        while queue_ds:
            level_list = []
            nodes_in_current_level = len(queue_ds)
            for i in range(nodes_in_current_level):
                current_node = queue_ds.pop(0)
                level_list.append(current_node)
                if current_node.left:
                    queue_ds.append(current_node.left)
                if current_node.right:
                    queue_ds.append(current_node.right)
            
            for i in range(1,nodes_in_current_level):
                level_list[i-1].next = level_list[i]
        return root
        """

        # Approach 2: without extra space
        first_element_of_level = root
        while first_element_of_level:
            current_element = first_element_of_level

            # for each node in a current level
            while current_element:
                print(current_element.val)
                # step 1: connect their child first (if exists)
                # at 1 connect 2-->3,
                # at 2 connect 4-->5
                # and at 3 connect 6-->7, and so on...
                if current_element.left is not None:
                    current_element.left.next = current_element.right

                # step 2: Before moving to the next element
                #       - connect left subtree and right subtree
                if current_element.next and current_element.right:
                    current_element.right.next = current_element.next.left
                # proceed with next element in the same level. 
                current_element = current_element.next
                
            # finally we move to leftmost element in the next level
            first_element_of_level = first_element_of_level.left

        return root
