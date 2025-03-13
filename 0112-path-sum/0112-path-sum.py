# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        print(targetSum)
        if not root:
            return False
        
        if root.left==None and root.right==None and root.val==targetSum:
            return True
        
        left_bool = self.hasPathSum(root.left,targetSum-root.val)
        right_bool = self.hasPathSum(root.right,targetSum-root.val)
        
        return left_bool or right_bool