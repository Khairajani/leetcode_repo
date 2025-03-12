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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
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