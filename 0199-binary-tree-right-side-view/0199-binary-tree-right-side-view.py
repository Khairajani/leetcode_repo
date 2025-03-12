# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        queue = [root]
        while queue:
            nodes_in_current_level = len(queue)
            for i in range(nodes_in_current_level):
                current_node = queue.pop(0)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
                if i==nodes_in_current_level-1:
                    result.append(current_node.val)
        return result