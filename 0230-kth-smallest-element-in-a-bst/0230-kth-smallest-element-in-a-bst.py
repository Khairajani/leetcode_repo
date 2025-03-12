# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        vector = []
        def inorder(root):
            if root:
                inorder(root.left)
                vector.append(root.val)
                inorder(root.right)
        inorder(root)
        return vector[k-1]
                
            
            