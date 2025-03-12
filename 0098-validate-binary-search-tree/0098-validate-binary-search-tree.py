# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, min_val, max_val):
        
        if node is None:
            return True
        
        if (min_val is not None and node.val<=min_val) or (max_val is not None and node.val>=max_val):
            return False
    
        return self.solve(node.left, min_val, node.val) and self.solve(node.right,node.val, max_val)
            

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.solve(root, None, None)
        

