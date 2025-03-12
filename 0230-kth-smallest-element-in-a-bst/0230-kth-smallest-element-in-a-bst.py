# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    count=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return None
        
        left = self.kthSmallest(root.left, k)
        if left is not None:
            return left
        self.count+=1
        if self.count==k:
            return root.val
        
        return self.kthSmallest(root.right,k)