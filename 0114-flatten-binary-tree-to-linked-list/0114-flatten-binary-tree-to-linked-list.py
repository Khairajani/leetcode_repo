# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        if root.left:
            left_subtree_right_leaf = root.left
            while left_subtree_right_leaf.right:
                left_subtree_right_leaf = left_subtree_right_leaf.right
            left_subtree_right_leaf.right = root.right
            root.right = root.left
            root.left = None
        
        self.flatten(root.right)
        return
