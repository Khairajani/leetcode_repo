# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root:    
            left_height = self.maxHeight(root.left)
            right_height = self.maxHeight(root.right)
            # because we want to get the path length and not number of nodes, that is why we are doing lh+rh and not 1+lh+rh
            self.diameter = max(self.diameter, left_height+right_height)       
            return max(left_height,right_height)+1
        else:
            return 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxHeight(root)
        return self.diameter        